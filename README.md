# Popular Locations Analysis using Hadoop MapReduce 🗺️

## 📖 Project Overview  
This project focuses on **pinpointing the most popular locations** in 2022 based on Airbnb listings. The analysis was performed using **Hadoop MapReduce** on the **Google Cloud Platform (GCP)**. The aim was to determine the top 5 locations with the highest number of reviews during the specified year.

---

## 🗂️ Dataset Details  
- **Dataset Source**: [Airbnb listings](https://drive.google.com/file/d/1KyZUXTaD5226CW5po3BCzLWmibBiGXYe/view?usp=drive_link)
- **Shape**: (87,946 rows × 75 columns)  
- **Preprocessing**:  
  - Python was used for data cleaning and preparation.  
  - Key columns utilized: `neighbourhood_cleansed`, `number_of_reviews`, `first_review`, and `last_review`.  
  - Created a new column `dates_2022` to filter reviews specific to the year 2022.  
  - Final dataset saved as: **`Review_counts_2022_final.csv`** with shape (15,789 rows × 3 columns).  

---

## 🔧 Approach and Workflow  

### **Data Cleaning Steps**  
1. Converted `first_review` and `last_review` columns to datetime format.  
2. Created a new column `dates_2022` to filter dates specific to 2022.  
3. Dropped rows where `dates_2022` was `Null`.  
4. Selected columns: `neighbourhood_cleansed`, `number_of_reviews`, and `dates_2022`.  

### **MapReduce Workflow**  
#### Mapper:  
- Processes input rows to map locations to their review counts.  
- **Key-Value Pair**: `Location → Review Count`  
#### Reducer:  
- Aggregates review counts for each location.  
- Outputs the top 5 locations with the highest number of reviews.  

### **Steps**  
1. **Input Split**: Each row of the dataset treated as input.  
2. **Mapping**: Mapped each location to its review count.  
3. **Shuffling**: Sorted the mapped data alphabetically by location.  
4. **Reducing**: Aggregated results to find the top 5 locations.  

---

## 💻 Platform and Tools Used  
- **Platform**: Google Cloud Platform (GCP)  
- **Cluster Service**: Dataproc  
- **Programming**: Python for data preprocessing and MapReduce scripts  
- **Commands**:  
  - Mapper.py  
  - Reducer_for_counts.py  

---

## 🔑 Execution Steps  
1. **File Upload**: Uploaded the dataset and MapReduce scripts to the cluster.  
2. **Execution**:  
   - Used `cat` and pipe (`|`) commands to execute the mapper.  
   - Sorted the mapper output using `sort`.  
   - Fed the sorted output into the reducer.  
3. **Output**:  
   - **Mapper Output**: Mapped locations to review counts.  
   - **Reducer Output**: Top 5 locations with the highest reviews in 2022.  

---

## 🏆 Results  
The top 5 locations with the highest number of reviews in 2022:  
1. **Westminster**  
2. **Camden**  
3. **Tower of Hamlets**  
4. **Kensington and Chelsea**  
5. **Southwark**  

---

## 🛠️ Unresolved Bottlenecks  
- **Case 1**: Unable to read files in HDFS.  
- **Case 2**: Stream command failed during execution.  
  - Ref: [StackOverflow Discussion](https://stackoverflow.com/questions/48003377/error-when-running-python-map-reduce-job-using-hadoop-streaming-in-google-cloud)  
  - Despite modifying the approach, the error persisted.  

---

## 📎 References  
- [Hadoop MapReduce in Python](https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/)  
- [Python on Hadoop - StackOverflow](https://stackoverflow.com/questions/15353252/running-the-python-code-on-hadoop-failed)  


## 🌍 Explore More Projects  
For more exciting machine learning and AI projects, visit **[The iVision](https://theivision.wordpress.com/)** and stay updated with the latest innovations and research! 🚀  

---
