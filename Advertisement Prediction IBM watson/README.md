# Create an application to predict your insurance premium cost with AutoAI 

## Login/Sign-up to IBM Cloud:  http://ibm.biz/insuranceChargesUsingAutoAI 


![finalDemo](https://user-images.githubusercontent.com/10428517/82013347-f7e71500-962e-11ea-9c28-2dec7d5b30cd.gif)


As shown above, this application leverages machine learning models to predict your insurance charges, and helps the customer understand how smoking or decreasing your BMI affects
insurance premiums.

As we see the value of gross insurance premiums worldwide continue to skyrocket past 5 trillion dollars,
we know that most of these costs are preventable. For example, just by eliminating smoking, and lowering
your BMI by a few points could mean shaving thousands of dollars off of your premium charges. In this 
application, we study the effects of age, smoking, BMI, gender, and region to determine how much of 
a difference these factors can make on your insurance premium.  By using our 
application, customers see the radical difference their lifestyle choices make on their insurance 
charges. By leveraging AI and machine learning, we help customers understand just how much smoking increases their premium, by predicting how much they will have to pay within seconds.

## Description

Using IBM AutoAI, you automate all the tasks involved in building predictive models for different requirements. You see how AutoAI generates great models quickly which save time and effort and aid in faster decision-making process. You create a model that from a data set that includes the age, sex, BMI, number-of-children, smoking preferences, region and charges to predict the health insurance premium cost that an individual pays.

When you have completed this code pattern, you understand how to:

* Setup, quickly, the services on IBM Cloud for building the model.
* Ingest the data and initiate the AutoAI process.
* Build different models using AutoAI and evaluate the performance.
* Choose the best model and complete the deployment.
* Generate predictions using the deployed model by making REST calls.
* Compare the process of using AutoAI and building the model manually.
* Visualize the deployed model using a front-end application.

### Architecture Components

![Architecture Components](https://media.github.ibm.com/user/21063/files/3b77e580-913c-11ea-9dea-425b1d4f4ee0)

## Flow Description
1. The user creates an IBM Watson Studio Service on IBM Cloud.
2. The user creates an IBM Cloud Object Storage Service and adds that to Watson Studio.
3. The user uploads the insurance premium data file into Watson Studio.
4. The user creates an AutoAI Experiment to predict insurance premium on Watson Studio
5. AutoAI uses Watson Machine Learning to create several models, and the user deploys the best performing model.
6. The user uses the Flask web-application to connect to the deployed model and predict an insurance charge.

## Included components
*	[IBM Watson Studio](https://cloud.ibm.com/catalog/services/watson-studio) - IBM Watson® Studio helps data scientists and analysts prepare data and build models at scale across any cloud.
*	[IBM Watson Machine Learning](https://cloud.ibm.com/catalog/services/machine-learning) - IBM Watson® Machine Learning helps data scientists and developers accelerate AI and machine-learning deployment. 
*	[IBM Cloud Object Storage](https://cloud.ibm.com/catalog/services/cloud-object-storage) - IBM Cloud™ Object Storage makes it possible to store practically limitless amounts of data, simply and cost effectively.

## Featured technologies
+ [artificial-intelligence](https://developer.ibm.com/technologies/artificial-intelligence/) - Build and train models, and create apps, with a trusted AI-infused platform.
+ [Python](https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language.



## Prerequisites

This Cloud pattern assumes you have an **IBM Cloud** account. Go to the 
link below to sign up for a no-charge trial account - no credit card required. 
  - [IBM Cloud account](https://ibm.biz/AutoAI-insurance)
  - [Python 3.8.2](https://www.python.org/downloads/release/python-382/)
  

# Steps
0. [Download the data set ](#step-0-Download-the-data-set)
1. [Clone the repo](#step-1-clone-the-repo)
2. [Explore the data (optional)](#step-2-explore-the-data-optional)
3. [Create IBM Cloud services](#step-3-create-ibm-cloud-services)
4. [Create and Run AutoAI experiment](#step-4-create-and-run-autoai-experiment)
5. [Create a deployment and test your model](#step-5-create-a-deployment-and-test-your-model)
6. [Create a notebook from your model (optional)](#step-6-create-a-notebook-from-your-model-optional)
7. [Run the application](#step-7-run-the-application)



## Step 1. Create IBM Cloud services

![Creating-Watson-Service](https://user-images.githubusercontent.com/54094367/111079988-d50ae300-8515-11eb-8616-bec6485c140c.gif)

1.	Login to your IBM Cloud account: http://ibm.biz/insuranceChargesUsingAutoAI 

2.	Within your IBM Cloud account, click on the top search bar to search for cloud services and offerings. Type in “Watson Studio” and then click on Watson Studio under “Catalog Results”.

3.	This takes you to the Watson Studio service page. Select a region, “Lite” plan (Free) and give your service a unique name. Click on “Create” and this creates a Watson Studio instance for you. 

4.	 Once the service instance is ready, you will be redirected to the Watson Studio page. Click on the “Get Started” button to launch Watson Studio in a new tab. This might take few minutes to set up the service. 

![Creating-empty-project](https://user-images.githubusercontent.com/54094367/111079989-d5a37980-8515-11eb-9cd0-cea012081dd3.gif)

5.	Under the heading “work with data” you will find a link that says, “Create a project”. Click on “Create a project”. Next, click on “Create an empty project”.

6.	On the new project page, give your project a name. You will also need to associate an IBM Cloud Object Storage instance to store the data set.

7.	Under “Select Storage Service”, click on the “Add” button. This takes you to the IBM Cloud Object Store service page. Leave the service on the “Lite” tier and then click the “Create” button at the bottom of the page. You are prompted to name the service and choose the resource group. Once you give a name, click “Create”.

8.	Once the instance is created, you’re taken back to the project page. Click on “refresh” and you should see your newly created Cloud Object Storage instance under Storage.

9.	Click the “Create” button at the bottom right of the page to create your project.

![Add-dataset](https://user-images.githubusercontent.com/54094367/111079986-d4724c80-8515-11eb-8d55-89185c9add23.gif)

10.	Click on the “Add to project” button on the top right corner. From the pop-up window select “Data”.

11.	In the column, on the right, click on “browse”. Navigate to the folder where you downloaded the data set to and select “insurance.csv”

12.	Watson Studio takes a couple of seconds to load the data, and then you should see the import has completed. To make sure it has worked properly, you can click on “Assets” on the top of the page, and you should see your insurance file under “Data Assets”.


## Step 4. Create and Run AutoAI experiment

![create-AutoAI-project](https://user-images.githubusercontent.com/54094367/111079982-d2a88900-8515-11eb-8b58-910c39785d27.gif)

1.	Once you have added the data set, click on the “Add to project” button on the top right corner. This time select “AutoAI experiment”.

2.	On the New AutoAI Experiment page, give a name to your project. 

3.	Next, you need to add a Watson Machine Learning instance. On the right side of the screen, click on “Associate a Machine Learning service instance”.

4.	On the Associate service page, click on the “New Service” button on the right side of the screen. From the pop-up screen, select “Machine Learning”.

5.	Select the appropriate region. It is recommended to build your machine learning service instance in the same region that you created your Watson Studio service. Select the “Lite” (free) plan. Give your instance a unique name. Click on “Create”.

6.	Once you create your machine learning service, on the next page, check the box with your machine learning service instance. Next, click on “associate service” on the right corner. 

7.	Once the service is successfully associated, you will be redirected to new AutoAI experiment page. Click on “Reload” on the right side of the screen. You should see your newly created machine learning instance. Click on “Create” on the bottom right part of your screen to create your first AutoAI experiment!

![settings-of-project](https://user-images.githubusercontent.com/54094367/111079981-d20ff280-8515-11eb-914f-7c4eddaeadcb.gif)

8.	After you create your experiment, you are taken to a page to add a data source to your project. Click on “Select from project” and then add the insurance.csv file. Click on Select asset to confirm your data source.

9.	Next, you see that AutoAI processes your data, and you see a What do you want to predict section. Select the expenses as the Prediction column.

10.	Next, let's explore the AutoAI settings to see what you can customize when running your experiment. Click on Experiment settings.First, you see the data source tab, which lets you omit certain columns from your experiment. You choose to leave all columns. You can also select the training data split. It defaults to 85% training data. The data source tab also shows which metric you optimize for. For the regression, it is RMSE (Root Mean Squared Error), and for other types of experiments, such as Binary Classification, AutoAI defaults to Accuracy. Either way, you can change the metric from this tab depending on your use case.

11.	Click on the Prediction tab from within the Experiment settings. There you can select from Binary Classification, Regression, and Multiclass Classification.

12.	Lastly, you can see the Runtime tab from the Experiment settings this shows you other experiment details you may want to change depending on your use case.

13.	Once you are happy with your settings, ensure you are predicting for the expense’s column, and click on the run Run Experiment button on the bottom-right corner of the screen.

14.	Next, your AutoAI experiment runs on its own. You see a progress map on the right side of the screen which shows which stage of the experiment is running. This may be Hyper Parameter Optimization, feature engineering, or some other stage.

15.	You have different pipelines that are created, and you see the rankings of each model. Each model is ranked based on the metric that you selected. In the specific case that is the RMSE(Root mean squared error). Given that you want that number to be as small as possible, you can see that in the experiment, the model with the smallest RMSE is at the top of the leaderboard.

![completed-pipeline](https://user-images.githubusercontent.com/54094367/111080010-e8b64980-8515-11eb-8feb-e464930ed949.png)

16.	Once the experiment is done, you see Experiment completed under the Progress map on the right-hand side of the screen.

![best-pipeline](https://user-images.githubusercontent.com/54094367/111080015-ebb13a00-8515-11eb-8cb2-b06d9b10c7dc.png)

17.	Now that AutoAI has successfully generated eight different models, you can rank the models by different metrics, by clicking on the drop-down next to “Rank by:” on the top right corner of the screen, such as explained variance, root mean squared error, R-Squared, and mean absolute error. Each time you select a different metric, the models are re-ranked by that metric.

![best-pipeline-features](https://user-images.githubusercontent.com/54094367/111079979-d1775c00-8515-11eb-97d3-7dfba7d85ff4.gif)

18.	In our case, we have RMSE as the experiment's metric. You see the smallest RMSE value is 4444.108, from Pipeline 4. Click on “Pipeline 4”.

19.	On the left-hand side, you can see different “Model Evaluation Measures”. For this particular model, you can view the metrics, such as explained variance, RMSE, and other metrics.

20.	On the left-hand side, you can also see “Feature Transformations”, and “Feature Importance”.

21.	On the left-hand side, click on “Feature Importance”. You can see here that the most important predictor of the insurance premium is whether you are a “smoker” or a “non-smoker”. This is by far the most important feature, with “bmi” coming in as the second most important. This makes sense, given that many companies offer discounts for employees who do not smoke.

## Step 5. Create a deployment and test your model

![deployment-space](https://user-images.githubusercontent.com/54094367/111079977-cfad9880-8515-11eb-8a80-2e37cdc4b678.gif)

1.	Once you are ready to deploy one of the models, click on “Save As” at the top-right corner of the model you want to deploy. Save it as a “Model” and name your model as you want. Click on “Create” 
Note: We show you how to save it as a notebook in step 6.

2.	Once the model is successfully saved, click on the “View in project” in the green notification on the right side of the screen. Alternatively, you can also find your model saved in the “Assets” tab under “Models”.

3.	Next, you are taken to a screen that has the overview of the model you just saved. Click on “Promote to deployment space” on the top right corner of your screen.  Alternatively, if you’re doing it from the Assets tab, then under the “Models” section, click on the 3 dots on the right side of your screen and click “promote”.

4.	On the Promote to space page, you need a target space to promote your model. Click on “New space +” on the right side of your screen. 

5.	Next, on the Create a deployment space screen, give your space a name, make sure the right cloud object storage is selected, and select your machine learning service instance. For this experiment, selecting the machine learning service is mandatory as we need to build a prediction model. Then click on “Create”.

6.	Once the space is ready, click on “Close” in the pop-up and you will be redirected to the promote to space page. You see your newly created space under the “Target space”. Once you’re happy with your selections, click on “Promote”. 

![deploy](https://user-images.githubusercontent.com/54094367/111079975-cf150200-8515-11eb-8dc0-89b06f4b6aa5.gif)

7.	Once the model is successfully promoted, you will see a green notification box, click on “deployment space” in the notification. Alternatively, you can also find your deployment spaces when you click on the hamburger sign on the top left most side on your screen. 

8.	You will be redirected to the deployments page, where you will find your promoted model. Hover over the row, to see a rocket shaped icon, click on the icon to deploy you model. 

9.	In the dialog box, select “Online” as your deployment type, give your deployment a name and click “Create”.

10.	Click on the “Deployments” tab to see the status of your deployment. 

![deployment-completed](https://user-images.githubusercontent.com/54094367/111080017-ece26700-8515-11eb-8b6d-7bb927b6bce8.png)

![test](https://user-images.githubusercontent.com/54094367/111079973-cd4b3e80-8515-11eb-9446-5d52a90bbf0e.gif)

11.	Once the deployment is completed, click on the name your deployment. 

12.	On this page you find the API references, endpoint and code snippets to help you integrate your model with your applications. 

13.	To test your model, click on the “Test” tab. You can select a row from the data set and enter the data in the fields. Enter the age, sex, bmi, children, smoker and region and then click on the “Predict” button at the bottom. 

14.	To validate the prediction, you check the data file that you used to train the model. As you can see, the model predicted a premium of 18524.04, when you enter age 19, bmi: 27.9, children: 0, smoker: yes, region: southwest. This is relatively close to the model's prediction, so we know the model is working properly.


## Step 6. Create a notebook from your model (optional)
#### If you want to run the notebook that you explore below, go to [`https://github.com/IBM/predict-insurance-charges-with-autoai/blob/master/notebooks/Insurance%20Premium%20Predictor%20-%20P8%20notebook.ipynb).
With AutoAI's latest features, the code that is run to create these models is no more a black box. One or more of these models can be saved as a Jupyter notebook and the Python code can be run and enhanced from within. 

### 6.1 Create notebook 
![create notebook](https://media.github.ibm.com/user/9960/files/1c47db00-8ae0-11ea-9066-9bb6137b6ee3)

* Click on `Save As` at the top-right corner of the model, and click `Notebook`. 

* This opens a new tab (be sure to enable pop-up for this website) titled `New Notebook` where in you can edit the default name if you choose to and then click on `Create`. This might take a few minutes to load for the first time. 

![also create notebook](https://media.github.ibm.com/user/9960/files/9a58b180-8ae1-11ea-97ca-f8ec5813f2ed)

* Alternatively, you can also create the notebook from the `Pipeline leaderboard` view (shown above) by clicking on the `Save as` option against the model you want to save followed by selecting `Notebook`. The steps are very similar to the first method discussed above. 



## Step 7. Run the application
The driver code to run the application can be found under the web-app folder within the git repository that was cloned from [Step 1](#step-1-clone-the-repo). To run and test your deployed model through this Python-based user-interface,
you need to replace the following information within `web-app/app.py`: 

1) Your Watson Machine Learning (which is associated with this deployed model) `Instance ID` and `apikey`.
1) Your deployed model's deployment URL, so you can make a POST request.
1) Your IBM Cloud IAM token, to authorize yourself. 

Now, you go into detail on how to gather these credentials. If you already know how to do this, you can
skip the steps below, and  go straight to running the application.


### 7.1 Get IBM Cloud API key

<!-- ![apikey-instanceID](https://media.github.ibm.com/user/79254/files/4119b680-8e30-11ea-8bc3-97ab1558fc23) -->
* Generate an IBM Cloud apikey by going to `cloud.ibm.com` and then from the top-right part of the screen click on `Manage`-> `IAM`.

![manage](https://user-images.githubusercontent.com/10428517/95252784-4d84af80-07d2-11eb-9fdd-1fe119329cef.png)


* Next, click on `API keys` from the left side-bar. Next click on `Create an IBM Cloud API key`.

![create-api-key](https://user-images.githubusercontent.com/10428517/95252429-d4855800-07d1-11eb-80e3-fd3b55d5d0a8.png)


* Name the key as you wish, and then click `Create`. 

![create](https://user-images.githubusercontent.com/10428517/95252417-d222fe00-07d1-11eb-95a9-8bd7c9d4bbce.png)


* Once the key is created, click on the `Download` button.

![download](https://user-images.githubusercontent.com/10428517/95252393-ccc5b380-07d1-11eb-8d14-9d7154f71b86.png)

