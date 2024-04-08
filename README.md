# PlotPilot
An GenAI powered Excel Add-In to generate Graphs

## Prerequisites

Before getting started, ensure you have the following prerequisites installed:

- **Node.js v18.18.2**: Visit the [Node.js site](https://nodejs.org/) to download and install.
- **Yeoman and the Yeoman generator for Office Add-ins**: Install using npm:

    ```bash
    npm install -g yo generator-office
    ```
- **Microsoft 365 subscription**: This includes Office on the web.
- **Vue.js**: Ensure Vue.js is installed on your system.
    ```bash
    npm install -g @vue/cli
    ```

## Setup

1. Clone the repository and navigate to the project directory frontend folder:

    ```bash
    git clone git@github.com:heushreck/PlotPilot.git
    cd PlotPilot/plot_pilot_frontend
    ```

2. Install dependencies:

    ```bash
    npm install
    ```

3. Run the project:

    ```bash
    npm run serve
    ```

## Sideloading the Excel Add-In

To integrate the Plot Pilot Add-In into Excel, follow these steps:

1. **Open Excel on the web**: Go to [https://www.office.com/launch/Excel](https://www.office.com/launch/Excel/?auth=2) and create a blank Workbook.

2. **Access Add-ins**: Select **Home** > **Add-ins**, then choose **More Add-ins**.

3. **Upload Add-in**: Within the **Office Add-ins** dialog, go to the **MY ADD-INS** tab, and select **Upload My Add-in**.

4. **Upload Manifest**: Browse to locate the add-in manifest file (*`PlotPilot/plot_pilot_frontend/manifest.xml`*), then select **Upload**.

5. **Confirmation**: After a few seconds, the Plot Pilot Add-In should appear in your Excel Home Bar.

6. **Access Add-In**: Open the add-in task pane in Excel. On the **Home** tab, select the **Plot Pilot** button.

Now you're ready to utilize Plot Pilot within Excel for enhanced data visualization capabilities!