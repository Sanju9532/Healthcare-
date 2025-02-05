#importing the libraries
import streamlit as st
import pandas as pd
import pymysql 
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

#title 
st.title("HEALTH CARE")

# Create a sidebar radio button for navigation options
page = st.sidebar.radio("Navigation", ["Home", "SQL QUERYS"])

#connecting mysql with python
mydb = mysql.connector.connect(
    host = "localhost",               # Host where the MySQL server is running
    user = "root",                    # Username to connect to the database
    password = "Sanjana@2003",         # Password for the MySQL user
    database = "healthcare",            # Name of the database to connect
    auth_plugin='mysql_native_password'  # Authentication plugin to use
)

# Creating  a cursor object to interact with the database
mycursor = mydb.cursor()

if page == "Home":

    #subheader 
    st.subheader("Dataset")
    dataset = mycursor.execute("select * from healthcares")  #executing the sql query
    datas = mycursor.fetchall()  # fetching all the results  
    # creating dataframe using the fetched data and specfing the column names
    table = pd.DataFrame(datas, columns=['Patient_ID','Admit_Date','Discharge_Date','Diagnosis','Bed_Occupancy','Test','Doctor','Followup_Date','Feedback','Billing_Amount','Health_Insurance_Amount'])
    #displaying a dataframe
    st.dataframe(table)



# Checking if the selected page is "SQL QUERIES"
if page == "SQL QUERYS":
    st.header("SQL QUERIES")
    #list of options for the user to select 
    select_options = st.selectbox("Select any question",['Query1','Query2','Query3','Query4','Query5','Query6','Query7','Query8','Query9','Query10','Query11','Query12','Query13','Query14','Query15'])
    # Creating a select box in the sidebar for the user to choose a query
    col = st.sidebar.selectbox("Select any query :",select_options)
    
    # Check the selected query

    if col == "Query1":
        # Execute a SQL query
        mycursor.execute("""
                         select month(Admit_Date) as admission_month,
                         year(Admit_Date) as admission_year,
                         count(*) as total_admission
                         from healthcares
                         group by admission_month,admission_year
                         order by total_admission desc
                        """)
                                                        
        counts = mycursor.fetchall()# fetching all the results  
        
        # creating dataframe using the fetched data and specfing the column names
        df = pd.DataFrame(counts,columns =['admission_month','admission_year','total_admission'])
        st.dataframe(df)

        # Create a bar chart
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Create a bar chart with admission_month and admission_year on the x-axis and total_admission on the y-axis
        ax.bar(df['admission_month'].astype(str) + '-' + df['admission_year'].astype(str), df['total_admission'],color = 'b')
        
        ax.set_xlabel('Admission Month-Year')
        ax.set_ylabel('Total Admissions')
        ax.set_title('Total Admissions by Month and Year')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        st.pyplot(fig)
        

    if col == "Query2":
        mycursor.execute("""
                         select diagnosis,
                         count(diagnosis) as "most_common_diagnoses" 
                         from healthcares 
                         group by diagnosis order by "most_common_diagnoses"
                         """)
        datas = mycursor.fetchall()# fetching all the results  

        # creating dataframe using the fetched data and specfing the column names
        df = pd.DataFrame(datas,columns=['diagnosis','most_common_diagnoses']) 
        st.dataframe(df)     

        fig,ax = plt.subplots(figsize = (5,3))
        ax.pie(df['most_common_diagnoses'],labels=df['diagnosis'],autopct = '%.2f%%') 
        circle = plt.Circle((0,0),0.50,fc='white')
        fi = plt.gcf()
        fi.gca().add_artist(circle)
        ax.set_title("Donet Chart for Diagnosis") 
        st.pyplot(fig)


    if col == "Query3":
        mycursor.execute("""
                        select Bed_Occupancy,
                         count(Bed_Occupancy) as "Bed_occupancy_count"
                         from healthcares 
                         group by  Bed_Occupancy
                         """)
        data = mycursor.fetchall()# fetching all the results  

        # creating dataframe using the fetched data and specfing the column names
        df = pd.DataFrame(data,columns=['Bed_Occupancy','Bed_occupancy_count'])
        st.dataframe(df)

        fig,ax=plt.subplots(figsize = (4,2))
        ax.pie(df['Bed_occupancy_count'],labels=df['Bed_Occupancy'],autopct='%.2f%%',startangle=50)
        ax.set_title("Pie Chart for Bed Occupancy")
        st.pyplot(fig)
    

    if col == "Query4":
        mycursor.execute("""
                         select  avg(datediff(Discharge_Date,Admit_Date)) as average_days,
                         max(datediff(Discharge_Date,Admit_Date)) as maximum_days 
                         from healthcares
                         """)
        datas = mycursor.fetchall()# fetching all the results  

        # creating dataframe using the fetched data and specfing the column names
        df=pd.DataFrame(datas,columns=['average_days','maximum_days'])
        st.dataframe(df)
        
        fig,ax =plt.subplots(figsize=(4,2))
        ax.pie(df['average_days'],labels=df['average_days'],colors = 'g')
        ax.set_title("Pie chart for Averagedays")
        st.pyplot(fig)
        
        fig,ax = plt.subplots(figsize=(4,2))
        ax.pie(df['maximum_days'],labels = df['maximum_days'],colors='r')
        ax.set_title("Pie chart for Maximumdays")
        st.pyplot(fig)


    if col == "Query5":
        mycursor.execute("""
                         select month(Admit_Date) as admission_month,
                         year(Admit_Date) as admission_year,
                         count(*) as total_admissions
                         from healthcares
                         group by admission_month,admission_year
                         order by admission_month,admission_year
                         """)
        data = mycursor.fetchall()# fetching all the results  

        # creating dataframe using the fetched data and specfing the column names
        df = pd.DataFrame(data,columns = ['admission_month','admission_year','total_admissions'])
        st.dataframe(df)

        # Create a bar chart
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Create a bar chart with admission_month and admission_year on the x-axis and total_admission on the y-axis
        ax.bar(df['admission_month'].astype(str) + '-' + df['admission_year'].astype(str), df['total_admissions'],color = 'black')
        
        ax.set_xlabel('Admission Month-Year')
        ax.set_ylabel('Total Admissions')
        ax.set_title('Total Admissions by Month and Year')
        plt.xticks(rotation=45)  # Rotating x-axis labels for better readability
        st.pyplot(fig)


    if col == "Query6":
        mycursor.execute("""
                         SELECT 
	                     patient_ID,
                         Diagnosis,
                         Admit_Date, 
                         Discharge_Date, 
                         DATEDIFF(Discharge_Date, Admit_Date) AS days_difference
                         FROM healthcare;
                         """)
        data = mycursor.fetchall()# fetching all the results  

        # creating dataframe using the fetched data and specfing the column names
        df = pd.DataFrame(data,columns=['patient_ID','Diagnosis','Admit_Date','Discharge_Date','days_difference'])
        st.dataframe(df)
        

    if col == "Query7":
        mycursor.execute("""
                         select distinct doctor,
                         feedback, 
                         count(feedback) as "Total_count"
                         from healthcares 
                         group by doctor,feedback
                         order by count(feedback) desc;
                         """)
        data = mycursor.fetchall()# fetching all the results  

        # creating dataframe using the fetched data and specfing the column names
        df  = pd.DataFrame(data,columns=['doctor','feedback','Total_count'])
        st.dataframe(df)



    if col == "Query8":
        mycursor.execute("""
                         select Diagnosis,
                         Test,
                         count(Diagnosis) as "counts_dig",
                         count(Test) as "counts_test"
                         from healthcares 
                         group by Diagnosis,Test
                         order by counts_dig desc,counts_test
                         """)
        data = mycursor.fetchall()

        # creating dataframe using the fetched data and specfing the column names
        df = pd.DataFrame(data,columns=['Diagnosis','Test','counts_dig','counts_test'])
        st.dataframe(df)


        fig,ax = plt.subplots(figsize=(5,3))
        ax.bar(df['Diagnosis'],df['counts_dig'],color='#FF5733')
        ax.set_title("Diagnosis by count of diagnosis")
        ax.set_xlabel('Diagnosis')
        ax.set_ylabel('counts_dig')
        plt.xticks(rotation = 45)    # Rotating x-axis labels for better readability
        st.pyplot(fig)

        fig,ax = plt.subplots(figsize=(5,3))
        ax.bar(df['Test'],df['counts_test'],color='b')
        ax.set_title("Test by count of Test")
        ax.set_xlabel('Test')
        ax.set_ylabel('counts_test')
        plt.xticks(rotation = 45)     # Rotating x-axis labels for better readability
        st.pyplot(fig)

    if col == "Query9":
         mycursor.execute("""
                          select doctor,
                          Diagnosis,
                          count(Diagnosis) as "counts_dig"
                          from healthcares
                          group by doctor,Diagnosis
                          order by count(Diagnosis)desc
                          """)
         data = mycursor.fetchall()# fetching all the results  

         # creating dataframe using the fetched data and specfing the column names
         df = pd.DataFrame(data,columns = ['doctor','Diagnosis','counts_dig'])
         st.dataframe(df)
         
         
    if col =="Query10":
        mycursor.execute("""
                         select patient_ID,
                         Diagnosis,
                         Discharge_Date,
                         Followup_Date,
                         datediff(Followup_Date,Discharge_Date) as checkup
                         from healthcares
                         group by patient_ID,Diagnosis,Discharge_Date,Followup_Date
                         """) 
        data = mycursor.fetchall()# fetching all the results  

        # creating dataframe using the fetched data and specfing the column names
        df = pd.DataFrame(data,columns=['patient_ID','Diagnosis','Discharge_Date','Followup_Date','checkup'])
        st.dataframe(df)


    if col == "Query11":
        mycursor.execute("""
                         select distinct Diagnosis,
                         doctor,
                         count(Diagnosis) as counts_dig
                         from healthcares
                         where doctor="Jay Sinha"
                         group by Diagnosis,doctor
                         """)
        data = mycursor.fetchall()# fetching all the results  

        # creating dataframe using the fetched data and specfing the column names
        df = pd.DataFrame(data,columns=['Diagnosis','doctor','counts_dig'])
        st.dataframe(df)

        fig,ax = plt.subplots(figsize=(5,3))
        ax.pie(df['counts_dig'],labels=df['Diagnosis'],autopct='%.2f%%')
        circle = plt.Circle((0,0),0.50,fc="white")
        fi = plt.gcf()
        fi.gca().add_artist(circle)
        ax.set_title("Percentage Distribution of Diagnoses")
        st.pyplot(fig)


    if col == "Query12":
        mycursor.execute("""
                         select distinct Diagnosis,
                         Bed_Occupancy,
                         count(bed_occupancy) as "count_bed_occupancy"
                         from healthcares 
                         group by Diagnosis,Bed_Occupancy
                         order by count(bed_occupancy)  desc
                         """)
        data = mycursor.fetchall()# fetching all the results  

        # creating dataframe using the fetched data and specfing the column names
        df = pd.DataFrame(data,columns = ['Diagnosis','Bed_Occupancy','count_bed_occupancy'])
        st.dataframe(df)
        fig,ax = plt.subplots(figsize = (5,3))
        ax.bar(df['Diagnosis'],df['count_bed_occupancy'],color = 'r')
        ax.set_title("Bed Occupancy Counts for Each Diagnosis")
        ax.set_xlabel("Diagnosis")
        ax.set_ylabel("count of bedoccupancy")
        plt.xticks(rotation=40)
        st.pyplot(fig)


    if col == "Query13":
        mycursor.execute("""
                         select patient_ID,
                         diagnosis,
                         Bed_Occupancy,
                         Billing_Amount 
                         from healthcares
                         order by Billing_Amount desc
                         """)
        data =  mycursor.fetchall()# fetching all the results  

        # creating dataframe using the fetched data and specfing the column names
        df = pd.DataFrame(data,columns=['patient_ID','diagnosis','Bed_Occupancy','Billing_Amount'])
        st.dataframe(df)
        fig,ax = plt.subplots(figsize = (5,3))
        ax.hist(df['Billing_Amount'],bins = 10)
        ax.set_xlabel("Billing Amount")
        ax.set_ylabel("Frequency")
        ax.set_title("Distribution of Billing Amounts")
        st.pyplot(fig)


    if col == "Query14":
        mycursor.execute("""
                         select * from healthcare where Bed_Occupancy in  ("General")
                         """)
        data = mycursor.fetchall()# fetching all the results  

        # creating dataframe using the fetched data and specfing the column names
        df = pd.DataFrame(data,columns = ['patient_ID','Admit_Date','Discharge_Date','Diagnosis','Bed_Occupancy','Test','Doctor','Followup_Date','Feedback','Billing_Amount','Health_Insurance_Amount'])
        st.dataframe(df)

        fig,ax = plt.subplots(figsize=(5,3))
        values = df['Diagnosis'].value_counts()
        ax.pie(df['Diagnosis'].value_counts(),labels=df['Diagnosis'].value_counts().index,autopct='%.2f%%')
        circle= plt.Circle((0,0),0.45,fc='white')
        figu = plt.gcf()
        fig.gca().add_artist(circle)
        ax.set_title("Distribution of Patient Diagnoses")
        st.pyplot(figu)


    if col == "Query15":
        mycursor.execute("""
                         select * from healthcares 
                         where Admit_Date between '2023-01-01' and '2023-02-01'
                         """)
        data = mycursor.fetchall()# fetching all the results  

        # creating dataframe using the fetched data and specfing the column names
        df = pd.DataFrame(data,columns = ['patient_ID','Admit_Date','Discharge_Date','Diagnosis','Bed_Occupancy','Test','Doctor','Followup_Date','Feedback','Billing_Amount','Health_Insurance_Amount'])
        st.dataframe(df)
        fig,ax = plt.subplots(figsize = (7,5))
        ax.hist(df['Admit_Date'],bins=30)
        plt.xticks(rotation = 35)
        ax.set_xlabel("Admit Date")
        ax.set_ylabel("Frequency")
        ax.set_title("Distribution of Admit Date")
        st.pyplot(fig)
    
                     
                             
                             
                             
                              
                              
                             
                             
            
        