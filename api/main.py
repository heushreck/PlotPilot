from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from enum import Enum
from openai import OpenAI
import instructor
import os

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChartType(str, Enum):
    Line = "Line"
    Doughnut = "Doughnut"
    ColumnClustered = "ColumnClustered"
    Waterfall = "Waterfall"
    XYScatter = "XYScatter"

class ChartData(BaseModel):
    title: str = Field(..., description="The title of the chart")
    x_axis_label: str = Field(..., description="The label for the x-axis")
    y_axis_label: str = Field(..., description="The label for the y-axis")
    chart_type: ChartType = Field(..., description="The type of chart")
    has_trendline: bool = Field(..., description="Whether the chart should has a trendline")

class ChartInputData(BaseModel):
    intention: str
    data: list

@app.post('/graph-data')
async def get_graph_data(chart_input_data: ChartInputData) -> ChartData:
    result = call_llm(chart_input_data)
    return result


def call_llm(input: ChartInputData) -> ChartData:
    try:
        # os.environ["OPENAI_API_KEY"] = ""
        client = instructor.from_openai(OpenAI())
        llm_response_model = client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_model=ChartData,
            messages=[
                {
                    "role": "system",
                    "content": "You are a talented data scientist."
                },
                {
                    "role": "user",
                    "content": "I need a chart that effectively represents my data. Please suggest a title, and labels for the x-axis and y-axis based on the chart's purpose, which is to {input.intention}. Also, select a chart type that best fits the data provided. Here is the data: {input.data}."
                },
            ]
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        llm_response_model = ChartData(title="Error", x_axis_label="Error", y_axis_label="Error", chart_type=ChartType.Line, has_trendline=True)
    return llm_response_model