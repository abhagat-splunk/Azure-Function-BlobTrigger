# Azure-Function-BlobTrigger
Azure function to detect changes to a blob storage container and send blob contents to Eventhub.

# Assumptions
This solution assumes you already have storage containers created and the have the path within it to monitor. The solution is designed to be tested on a development Splunk instance before being deployed to production.

# Requirements
* Eventhub Connection String
* Blob Storage String
* Blob container to monitor
* Visual Studio Code

# Explanation
Programs like Application Insights tend to push data into blob stograge containers. For SIEM applications like Splunk to index these files for further analysis, the Azure-Function-Blob trigger is a reactive solution. Sensitive to changes within a blob root container, the function will be triggered as new files are added to it. The function contains bindings to Eventhub that then holds these changes for the Microsoft Cloud Services Add-on for Splunk to retrieve.

# Usage
* Download the code from the repo : [Azure-Function-BlobTrigger](https://github.com/xynazog/Azure-Function-BlobTrigger)
* In VSCode, open the project Azure-Function-BlobTrigger.
* Install the [Azure Functions Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) for VSCode.
* If you do not have Eventhub configured, create one from [Azure Portal](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-create)
* Retrieve the connection string for Eventhub from the [Portal](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-get-connection-string#get-connection-string-from-the-portal) and update the [local.settings.json](https://github.com/xynazog/Azure-Function-BlobTrigger/blob/main/local.settings.json) file's `splunkmscsdev_EVENTHUB` field.
* Replace the [function.json](https://github.com/xynazog/Azure-Function-BlobTrigger/blob/main/send_data_to_hec/function.json) file's `<Insert-EventHub-name-here>` text to the Eventhub name configured on Step 4.


# Testing
* Retrieve a _*test*_ blob storage container connection string from the [Portal](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-dotnet#copy-your-credentials-from-the-azure-portal) and update the [local.settings.json](https://github.com/xynazog/Azure-Function-BlobTrigger/blob/main/local.settings.json) file's `splunkmscs_STORAGE` field.
* Replace the [function.json](https://github.com/xynazog/Azure-Function-BlobTrigger/blob/main/send_data_to_hec/function.json) file's `<Insert-container-name-here>` text to the root container to monitor.
* Configure the Splunk Add-on for Microsoft Cloud Services for the [Eventhub Input](https://docs.splunk.com/Documentation/AddOns/released/MSCloudServices/Configureeventhubs). Set the Input to monitor for the Eventhub configured on Step 4.
* The function is now ready to be tested. Press F5 to build the project locally.
* To test, configure the Splunk Add-on to send data to a test index. 
* Upload a sample file to a test container from the Azure portal and check Splunk to see the data come into the test index.
* Once the test has passed, configure the solution to work for a production blob storage container.
