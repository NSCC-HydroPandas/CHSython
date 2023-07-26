# CHSython

Installation:
Software requirements:
Python v3.5.4
CHSython application
1.	Install Python v3.5.4 from https://www.python.org/downloads/release/python-354/
2.	Copy CHSython to a newly created C:\Tools folder
3.	Browse to C:\Tools\CHSython and right click the Install.bat and open with Notepad ++ or Notepad
4.	Browse to the location on your pc where Python has been installed. Choose the Python\Python35\scripts location and copy this location. The pip.exe file within this location will download additional libraries required for the application to function.
5.	Within Install.bat, replace the default path on Line 1 with the path you just copied from your local machine.
6.	Save Install.bat
7.	On line 12 through 16 of Install.bat, verify that the geopandas files are calling the same directory as they are on your local machine. If they are not, then you will need to replace the file location to match that of your local pc. If CHSython was placed in C:\Tools\CHSython as noted above, no changes will be required.
8.	Save and close Install.bat
9.	Double click Install.bat to install the CHSython program
10.	Ensure the CHS Spatial Reference file is added to the C:\ProgramData\CARIS\HIPS and SIPS\11.4\System. Copy from N:\HIC1\Software_Manuals\Caris\HIPS\CHS_Specific_Spatial_ref
11.	Change paths to match software installed on your computer. Do not change Base 4 (This is only used  during the conversion of Base 5 surfaces to Base 4 surfaces and is no longer required step) 
![image](https://github.com/HydroPanadas/CHSython/assets/80972086/60c22eee-f873-437e-ae9d-4ea1f47f680d)

12.	Starting CHSython Application:
a.	Right Click on CHSython.py
b.	Select Edit with Idle 3.5 (64 bit)
c.	File Menu- Select Run – Run Module or F5

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/c524f673-b966-4806-8b6a-487ad4c58fd2)


14.	Checking Julian Day
Additional Tools – DOY to JD
Specify Year, Day and Month

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/5975cb83-308c-4d4b-b859-c6d28fd55b91)

16.	Create Project Directory
Fill in Project Name. Format is very important. Project Name – CHSDir#_Location_Year_Vessel_Sounder (must have all the elements)

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/1708e4bb-6248-4396-bc29-b049f6a4b302)

Additional Tools – Create Proj Dir - Specify Location to Create Folder when the window appears

15.	HIPS Project Settings
***Important Ensure File Paths have no Spaces use _***
RAW Sonar Data Folder – Location of Day’s Sonar Files (point to JD folder of Raw Data)
Processing/ HDCS_Data Folder – Location to Create and Save HIPS File
Output folder – Dump Location Caris Logs and other output
Project Name – CHSDir#_Location_Year_Vessel_Sounder (must have all the elements)
Vessel Config File – Select the Vessel File
Choose CRS – Select Survey CRS
i.	Remember CANNET – NAD83(CSRS) Epoch 2010 MARINSTAR – ITRF 2014 Epoch 2010
Julian Day and Year – Specify Julian Day and Year
If this is the initial run for the survey please select initial run this will ensure the HIPS file is in desired CRS

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/24489718-d12d-41af-8b49-96f72261a755)

16.	Processing Settings

a.	Select Processes to Run
Convert Sensor Data – Select Sensor Type
Import Applanix Data – Select Positioning Method
Geo-reference
Apply Tide – Select Tide Reduction
Compute TPU -  Select TPU
Apply SVP – Select if SV not applied in Real Time

Select Grid Creation
Create HIPS Grid – First Day of Survey
Create/Add to HIPS Grid – Following Days

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/7bcd64ba-d263-4a41-bba6-97e9b1616819)

17.	Use The Tabs to set Process Specific Settings

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/a5e3d856-4006-46fd-87c4-928983aa191b)

a.	Import Sensor Data
All Options disabled but available for viewing purposes

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/0cdc937d-e023-4ac0-98b8-931a59c13ca6)

  b.	Import Applanix Data
  Select the File Location for POS Files or SBET/RMS Files Depending on Processing Method (Note warning about settings on right of window)
  Select the reference week/day

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/d4f8d012-59d6-44ce-b17c-06dfefb13c33)

c.	Apply Tides
Select the File Location for the Tides .txt file and the .info file
Select the correct Model CRS. 
NAD 83 (CSRS) - EPSG 4617 
ITRF 2014 - EPSG 7912

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/2ed7c4d0-fad3-47e6-becf-66fb6432c4ea)

d.	Compute TPU
Set the TPU parameters for survey following the TPU user message, specs, and equipment used during survey
-	Ensure “m” is within resolution

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/693c8264-55c2-471c-86b3-45b3f9f4b3a2)

e.	Apply SVP 
If SV is not applied in real time. 

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/5351c4fa-5163-4c85-a340-beeb23863a53)

f.	Gridding
Set the resolution and Surface Directory. This will only need to be done once if you save your parameters after the first run.
***This will tie PACD to the surfaces***
 
 ![image](https://github.com/HydroPanadas/CHSython/assets/80972086/19f3b675-5fcf-456f-8592-68f52fe7120e)

18.	Merging Only
Specify the Vertical Reference system
This will only merge the lines by day and will not apply any of the Georeferencing steps to the data. This is only suggested to use if there is a need to merge an entire day that has already had geo-referencing steps applied or for a quick merging to view the point cloud before applying and geo-referencing steps.
Currently in development is the option to select multiple track lines across any of the Julian days of the project and merge that list only, instead of by day

19.	Reporting Creating Daily and Weekly Reports    
•	Ensure that Create Hips grid option in selected so that the surface directory is specified
•	Specify Location of Daily Report Spreadsheet- Create a Spreadsheet if first day
•	Specify Location of Weekly Report Spreadsheet - Create a Spreadsheet if first day
o	For each week provide a sheet a name within the weekly, save and close spreadsheet
  
![image](https://github.com/HydroPanadas/CHSython/assets/80972086/a98b1432-0386-414e-87cc-749ca0be0c79)
  
•	Set the Survey week sheet to correct sheet Week#, JD#-JD# 
•	Set IHO Order from Survey Instructions
•	If this is the first day of Survey Select the Create New Sheet
•	Set the QC type (Surface is much faster and only does TVU where the HIPS point QC looks at the entire point cloud and does both TVU and THU.

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/e2a679a0-ca33-4abb-bf3c-a4c47920a8e3)

*Run individually  by using the Create Daily, Weekly Reports Button or with Caris Processing using the Process Data Button

20.	Save Parameters
File- Save Parameters
File- Close Application will also prompt to save

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/7e4b183a-85ee-4357-b30e-9e1eea711b89)![image](https://github.com/HydroPanadas/CHSython/assets/80972086/ad60a5a8-7d82-4321-a83c-da000750e8ae)

21.	POSPAC Processing
POS File Folder- Directory Location of POS Files
GNSS Receiver Observation File – File Location of Base Station observation File
PPP Lat D-M-S – NRCAN PPP Computed Latitude Coordinate
PPP Long D-M-S – NRCAN PPP Computed Longitude Coordinate*
	*Notice no negative sign in West coordinate
PPP Height Metres – NRCAN PPP Height Metres
Corrections/Base Station Reference Frame – Reference Frame for GNSS corrections and SBET export.
Ensure Project Name, Output folder and Julian Day are set

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/1c2b9976-fbe1-4a10-81a7-d9ec44c2ddc0)

Copy  POSPAC Batch file “JD#_Vessel_System.posbat” to location desired to create POSPAC project. 
Open POSPAC and Run JD#_Vessel_System.posbat.
Project Tab- Batch Manager 

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/f613ea38-6433-40cd-882b-41881bca16c0)

Batch Manager window – Load Batch file – Right click Run

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/5395e533-a88f-4832-b506-d2e5c73189de)

22.	Finalization and Submission
Creates finalized Surfaces in Base 4 and Hips 11 Format, VALSRC Meta data form (1001-07-A-F02) for each Surface.
Save all surfaces for finalizing into VALSRC folder and named appropriately
If submission required for BDB 4 check the Convert surface to BASE 4.4 box ***Must have BDB installed***
If processing surface for Arctic (i.e surfaces are in WGS84/EPSG Canada Polar Stereographic: EPSG:5937 Epoch 2010 and are require to be in ITRF2008 Epoch 2010, and cut using the Artic Tiles then select the Artic processing box
Enter SURSTA (Survey Start Date) and SUREND (Survey End Date)
Enter a POSSAC Value – Subsample Query using Subset
Enter the POSHDW, TECPOS, and Collection Method metadata
The SOUACC is computed automatically using a weighted mean of the uncertainty band with the depth band used as the wights. Please see SOUACC_Weightedmean.docx for explanation. 

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/8258e7ef-7b31-4d97-8ad3-d5f811550c68)

Output Atlantic Processing
1.	Finalized surfaces under a Finalized surface folder. 
a.	Depth layer only for Atlantic processing
b.	Depth and Uncertainty bands Arctic processing
2.	Bounding Polygons for each surface in shapefile format that can be attached manually to the finalized surface with all holes removed (VALSRC#cvrage(A)_FinalBP.shp)
3.	Completed ISO 1001-07-F01 VALSRC Metadata form for each surface
4.	QC of final Surfaces
a.	Plots of surfaces uncertainty band (TVU) compared to each survey order

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/a798df93-0017-4644-951e-fdfdcc18da61)

b.	Caris TVU QC Report in CSV format for each surface

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/5a662610-8b49-4ef5-a0c6-7b34db400a06)

6.	Arctic Processing Only
a.	Finalized surfaces transformed to ITRF2008 Epoch 2010 and cut to the Arctic Tiles

23.	ATL ISO 1001-07-AFO1 Data Submission Form
Provide Intails, and the Project directory location (...9XXXXX_Location_Year)
 
![image](https://github.com/HydroPanadas/CHSython/assets/80972086/829afeef-b4c5-49f7-af6b-27051c7562f1)

24.	Bounding Polygon
Specify the Surface folder – Bounding polygons for surfaces will be created in shapefile format and can be attached manually in either HIPS or BASE. 
***This has worked well with Multibeam Datasets only***

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/48803557-ef2d-4ee9-bc91-267f6e134bc3)

25.	Refraction Editing
Remember Data should be cleaned and tool only used across smooth seafloors to mitigate refraction errors
Specify Number of Profiles to Create
Select Trackline Directory
Press Compute Refraction Coefficients
If the Entire Line is to be corrected (No Sloped section of rocky areas) no need to use Edit Refraction Coefficients
Select an option of where the desired coefficients should be set to 0
Specify Profile Number taken from a Subset Selection for each line
		Apply Refraction Coefficients to selected lines through Georeference
			Select Vertical Reference Type
			Select Vessel File

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/606db3f0-fe9b-4e0a-b078-7e3c3c9164c2)

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/e706b1bc-e80f-4547-9037-408ac1080431)

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/4129bbaf-49cc-4c5b-98c0-676fb66cf1d3)

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/a9e194eb-ea2c-4dd9-8fbc-a6c376287737)

26.	Smooth Heave
Can only be ran on a line by line bases due to BUG in Caris HIPS 11.3.5
This apply smoothing to Heave and Delayed Heave then remerges the Line
Run through Process Designer in HIPS

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/b342ffae-55ff-4eab-b8b5-6fc4acef1c18)

27.	HIPS 11 to BASE 4
This will convert HIPS 11 or BASE 5 surfaces into Base 4 compatible surfaces for BDB 4
Save FINALIZED HIPS 11 Surfaces to a folder, select folder in GUI
Press Run

![image](https://github.com/HydroPanadas/CHSython/assets/80972086/fe3b1947-c44e-4918-920f-4be13e0e833d)

For help with NAVWARN tools, Bounding Polygon, Extract tool and others please see corresponding power point help files.
