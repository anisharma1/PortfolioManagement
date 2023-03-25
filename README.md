# PORTFOLIO MANAGEMENT PROJECT
## (ASCEND EduCare Group 3)
* ### ABOUT<br>
   * The portfolio management application is a comprehensive platform that facilitates investment tracking <br> and performance monitoring for users. The application offers a user-friendly interface, which displays<br> the user's holdings, transactions, and performance metrics.
   * It is built on django framework and uses sql database.
   * The portfolio management project has been extended to develop an analysis tool to enable the user to effectively monitor his/her investments and make informed futher investment decisions.
   * The analysis tool has been developed using Google Colab and ipywidgets library.
 <hr>
 
 
* ### TABLE OF CONTENTS
   * [GETTING STARTED](https://github.com/Snehil0603/PortfolioManagement/blob/main/README.md#getting-started)
   * [OVERVIEW](https://github.com/Snehil0603/PortfolioManagement/blob/main/README.md#overview)
   * [FUTURE SCOPE](https://github.com/Snehil0603/PortfolioManagement/blob/main/README.md#future-scope)
   * [OUR GROUP](https://github.com/Snehil0603/PortfolioManagement/blob/main/README.md#our-group)
   
 <hr>  
   
   
* ### GETTING STARTED
  * #### INSTALLATION
    * We need Python, Django and mysqlclient installed to run this project.
      * Python : <a href="https://www.python.org/downloads/">Python Installation</a>
      * Django : `pip install django`
      * MySQLClient : <a href="http://dev.mysql.com/downloads/shell/">MySQLClient Installation</a>
   * <b>After installing the dependencies -:</b>
      * Clone the repository :
        * `git clone https://github.com/<username>/<forked-repo>.git`
       * Create your own virtual environment : 
         * `python3 -m venv venv`
         * 'source venv/bin/activate'
       * Install your requirements :
         * `pip install -r requirements.txt`
       * open cmd and run the commands to create the database :
         * `mysql -u root -p`
         * `CREATE DATABASE portfoliomanagement;`
         * `USE portfoliomanagement;`
       * To get database files in your PC run this command for all .sql files in database folder :
          * `mysql > source file_path_with_file_name.sql;`
       * Open setting.py file in PortfolioManager folder and change database section to this : 
       <img src="https://user-images.githubusercontent.com/96441611/227181216-391d9495-4f78-4682-9a22-687cf4cf38c1.png"></img>
       * Make your migrations : 
          * python manage.py makemigrations
          * python manage.py migrate
        * Run project on localhost : 
          * python manage.py runserver<br>
<hr>
    
 * ### OVERVIEW
    * ### REGISTER
      <img src="https://user-images.githubusercontent.com/111197294/227714950-55ed6f37-df06-4924-b74d-3f066fbe4e61.png" width="600"></img>
    * #### HOME
      <img src="https://user-images.githubusercontent.com/96441611/227183299-162c32a3-8162-4d6c-8da4-a167eea1c162.png" width="600"></img>
    * #### DASHBOARD
      <img src="https://user-images.githubusercontent.com/96441611/227183321-2a2e96e0-e77d-4cc0-8a71-550047cd7311.png " width="400"></img>
    * #### ALL_STOCKS_PROFILES
       <img src="https://user-images.githubusercontent.com/96441611/227183334-5d7c7422-13c8-4ee3-9368-5b4c751419de.png" width="400"></img>
    * #### MY STOCKS
      <img src="https://user-images.githubusercontent.com/96441611/227191119-9d318de5-b9f3-4073-8466-f0c355740034.png" width="400"></img>
    * #### LOGOUT
    <img src="https://user-images.githubusercontent.com/96441611/227191421-219aabaf-2726-4502-ae38-c2b12259cc76.png" width="400"></img>
<hr>

 * ### FUTURE SCOPE
    * The future endeavors associated with the application include integrating analysis of specific stocks with<br> our web app and expanding the range of investment types supported, integrating advanced analytics and reporting, and<br> collaborating with third-party investment tools.
<hr>




 * ### OUR GROUP
   * #### ISHANK JAIN (MENTOR)
   * #### RISHIKA 
   * #### NIHARIKA
   * #### SNEHIL
   * #### ANISHA SHARMA
   * #### KOMAL
    
  




