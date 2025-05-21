# Tracking 287(g)

This repository downloads data from the **287(g)** program and organizes it to be used by journalists, advocates, and the public. The scraper runs daily, extracting data from the official [ICE 287(g) page](https://www.ice.gov/identify-and-arrest/287g). The data is saved in two main folders:

- **`agreements/`**: Contains PDFs of all 287(g) agreements between law enforcement agencies and ICE, categorized by download date/time, state, and agency.
- **`sheets/`**: Stores Excel files listing participating and pending agencies, as published on the ICE website, categorized by download date/time.

### *Note*
This project was created in my personal capacity. Should you have any questions or suggestions for other public immigration data you would like to see tracked, you can contact me at elijahappelson@gmail.com. 


## Purpose

Law enforcement agencies are increasingly entering into agreements with ICE under the **287(g)** program, assisting in the deportation of immigrants from across the U.S. This program is supported by mandates like [Louisiana Executive Order Number JML 25-060: Project Geaux](https://interactive.wwltv.com/pdfs/Operation_GEAUX.pdf), which directs state law enforcement agencies to collaborate with ICE.

As mandates like this continue to grow, it’s crucial to track which agencies are involved in the program, especially as the Federal Government continues to make data harder to access. This repository provides a real-time overview of participating agencies and their respective agreements.

### *Note*
The Immigration Legal Resource Center maintains a [national map](https://www.ilrc.org/practitioners/national-map-287g-agreements) of 287(g) agreements along with resources to  understand them. 

## Setup

To use this repository, follow these steps:

### 1. Clone the repository
Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/tracking-287g.git
```

### 2. Install dependencies
Ensure you have Python installed on your system. Then, install the necessary dependencies by running:

```bash
pip install -r requirements.txt
````
### 3. Run the scraper
To start the scraper, run the following command:

```bash
python scraper.py
```

## File Structure

- `.github/workflows/run_scripts.yaml`: GitHub Actions workflow file used for automating the execution of the scraper script.
- `scraper.py`: The Python script responsible for scraping 287(g) data from the ICE website.
- `agreements/`: Directory that stores the PDF agreements between ICE and law enforcement agencies.
- `sheets/`: Directory that stores the excel files with data on participating and pending agreements between ICE and law enforcement agencies.
- `requirements.txt`: Text file listing all Python dependencies required to run the scraper.
- `README.md`: This file.


## Pending Agencies:

### State: ALABAMA
  - **Houston County Sheriff's Office**
  - **Lawrence County Sheriff's Office**
  - **Lawrence County Sheriff's Office**
  - **Level Plains Police Department**
  - **Limestone County Sheriff's Office**
  - **Pike County Sheriff's Office**

### State: ARIZONA
  - **Yuma County Sheriff's Office**

### State: FLORIDA
  - **Apopka Police Department**
  - **Atlantis Police Department**
  - **Cape Coral Police Department**
  - **Casselberry Police Department**
  - **Cocoa Police Department**
  - **Eatonville Police Department**
  - **Edgewater Police Department**
  - **Fellsmere Police Department**
  - **Florida Department of Agriculture**
  - **Florida International University Police Department**
  - **Hialeah Police Department**
  - **Hollywood Police Department **
  - **Lake Mary Police Department**
  - **Longboat Key Police Department**
  - **Palm Springs Police Department**
  - **Pensacola Police Department**
  - **Rockledge Police Department**
  - **Sanford Police Department**
  - **Satellite Beach Police Department**
  - **University of North Florida Police Department**
  - **West Palm Beach Police Department**
  - **Windermere Police Department**
  - **Winter Springs Police Department**

### State: GEORGIA
  - **Catoosa County Sheriff's Office**
  - **Catoosa County Sheriff's Office**
  - **Coweta County Sheriff's Office**
  - **Dawson County Sheriff's Office**
  - **Harris County Sheriff's Office**
  - **Jasper County Sheriff's Office**
  - **Jasper County Sheriff's Office**
  - **Monroe Police Department**
  - **Montgomery County Sheriff's Office**
  - **Murray County Sheriff's Office**
  - **Spalding County Sheriff's Office**

### State: KANSAS
  - **Anderson County Sheriff's Office**
  - **Haskell County Sheriff's Office**

### State: MARYLAND
  - **Allegany County Sheriff's Office**

### State: MICHIGAN
  - **Roscommon County Sheriff's Office**

### State: MINNESOTA
  - **Mille Lacs County Sheriff's Office**

### State: MISSOURI
  - **Christian County Sheriff's Office**

### State: MONTANA
  - **Cascade County Sheriff's Office**

### State: NEVADA
  - **Lyon County Sheriff's Office**
  - **Lyon County Sheriff's Office**

### State: OKLAHOMA
  - **Oklahoma Department of Corrections**
  - **Oklahoma Department of Corrections**

### State: PENNSYLVANIA
  - **Butler County Sheriff's Office**

### State: STATE
  - **LAW ENFORCEMENT AGENCY**

### State: TENNESSEE
  - **Tennessee Department of Corrections**
  - **Bradley County Sheriff's Office**
  - **Macon County Sheriff's Office**
  - **Sullivan County Sheriff's Office**

### State: TEXAS
  - **Anderson County Sheriff's Office**
  - **Colorado County Sheriff's Office**
  - **Denton County Sheriff's Office**
  - **Franklin County Sheriff's Office**
  - **Milam County Sheriff's Office**
  - **Rains County Sheriff's Office**
  - **San Jacinto County Sheriff's Office**

### State: VIRGINIA
  - **Alleghany County Sheriff's Office**

### State: WISCONSIN
  - **Walworth County Sheriff's Office**

### State: WYOMING
  - **Carbon County Sheriff's Office**
  - **Laramie County Sheriff’s Office**

## Participating Agencies:

### State: ALABAMA
  - **Colbert County Sheriff's Office**
  - **Colbert County Sheriff's Office**
  - **Crenshaw County Sheriff's Office**
  - **Elmore County Sheriff's Office**
  - **Etowah County Sheriff's Office**
  - **Franklin County Sheriff's Office**
  - **Henry County Sheriff's Office**
  - **Henry County Sheriff's Office**
  - **Franklin County Sheriff's Office**

### State: ALASKA
  - **Alaska Department of Corrections**
  - **Kodiak Police Department**

### State: ARIZONA
  - **Arizona Department of Corrections**
  - **La Paz County Sheriff's Office**
  - **La Paz County Sheriff's Office**
  - **Mesa Police Department**
  - **Navajo County Sheriff's Office**
  - **Pinal County Sheriff's Office**
  - **Yavapai County Sheriff's Office**

### State: ARKANSAS
  - **Benton County Sheriff's Office**
  - **Craighead County Sheriff's Office**

### State: COLORADO
  - **Teller County Sheriff's Office**

### State: FLORIDA
  - **Alachua County Sheriff's Office**
  - **Alachua County Sheriff's Office**
  - **Arcadia Police Department**
  - **Baker County Sheriff's Office**
  - **Auburndale Police Department**
  - **Baker County Sheriff's Office**
  - **Bay County Sheriff's Office**
  - **Bartow Police Department**
  - **Bay County Sheriff's Office**
  - **Belle Isle Police Department**
  - **Belleair Police Department**
  - **Bradford County Sheriff's Office**
  - **Brevard County Sheriff's Office**
  - **Blountstown Police Department**
  - **Broward County Sheriff's Office**
  - **Boca Raton Police Department**
  - **Calhoun County Sheriff's Office**
  - **Boynton Beach Police Department**
  - **Charlotte County Sheriff's Office**
  - **Bradenton Police Department**
  - **Citrus County Sheriff's Office**
  - **Bradford County Sheriff's Office**
  - **Brevard County Sheriff's Office**
  - **Broward County Sheriff's Office**
  - **Clay County Sheriff's Office**
  - **Clay County Sheriff's Office**
  - **Calhoun County Sheriff's Office**
  - **Collier County Sheriff's Office**
  - **Columbia County Sheriff's Office**
  - **Charlotte County Sheriff's Office**
  - **Chattahoochee Police Department**
  - **Citrus County Sheriff's Office**
  - **City of Miami Springs Police Department**
  - **City of St. Cloud Police Department**
  - **City of Zephyrhills Police Department**
  - **DeSoto County Sheriff's Office**
  - **Clay County Sheriff's Office**
  - **Dixie County Sheriff's Office**
  - **Clearwater Police Department**
  - **Clermont Police Department**
  - **Escambia County Sheriff's Office**
  - **Cocoa Beach Police Department**
  - **Flagler County Sheriff's Office**
  - **Collier County Sheriff's Office**
  - **Florida Department of Corrections**
  - **Columbia County Sheriff's Office**
  - **Coral Gables Police Department**
  - **Davenport Police Department**
  - **Davie Police Department**
  - **Daytona Beach Police Department**
  - **Daytona Beach Shores Public Safety**
  - **Deland Police Department**
  - **DeSoto County Sheriff's Office**
  - **Franklin County Sheriff's Office**
  - **Dixie County Sheriff's Office**
  - **Gadsden County Sheriff's Office**
  - **Gilchrist County Sheriff's Office**
  - **Edgewood Police Department**
  - **Glades County Sheriff's Office**
  - **Escambia County Sheriff's Office**
  - **Gulf County Board of County Commissioners**
  - **Eustis Police Department**
  - **Hamilton County Sheriff's Office**
  - **Flagler County Sheriff's Office**
  - **Hardee County Sheriff's Office**
  - **Florida A&M University Board of Trustees**
  - **Hendry County Sheriff's Office**
  - **Florida Department of Environmental Protection**
  - **Hernando County Sheriff's Office**
  - **Hernando County Sheriff's Office**
  - **Florida Department of Financial Services**
  - **Florida Department of Highway Safety and Motor Vehicles, Division of Highway Patrol**
  - **Florida Department of Law Enforcement**
  - **Highlands County Sheriff's Office**
  - **Florida Department of Lottery Services **
  - **Hillsborough County Sheriff's Office**
  - **Florida Division of Alcoholic Beverages and Tobacco**
  - **Florida Fish and Wildlife Conservation Commission**
  - **Florida Gaming Control Commission**
  - **Holmes County Sheriff's Office**
  - **Florida Gulf Coast University Police Department**
  - **Florida National Guard**
  - **Indian River County Sheriff's Office**
  - **Florida Polytechnic University Police Department**
  - **Florida Southwestern State College Police Department**
  - **Florida State Guard**
  - **Fort Walton Beach Police Department**
  - **Jackson County Correctional Facility**
  - **Jacksonville Sheriff's Office**
  - **Jefferson County Sheriff's Office**
  - **Franklin County Sheriff's Office**
  - **Ft. Myers Police Department**
  - **Gadsden County Sheriff's Office**
  - **Gilchrist County Sheriff's Office**
  - **Glades County Sheriff's Office**
  - **Lafayette County Sheriff's Office**
  - **Green Cove Springs Police Department**
  - **Lake County Sheriff's Office**
  - **Gulf Breeze Police Department**
  - **Gulf County Sheriff's Office**
  - **Lee County Sheriff's Office**
  - **Lee County Sheriff's Office**
  - **Gulfport Police Department**
  - **Leon County Sheriff's Office**
  - **Hamilton County Sheriff's Office**
  - **Levy County Sheriff's Office**
  - **Liberty County Sheriff's Office**
  - **Hardee County Sheriff's Office**
  - **Havana Police Department**
  - **Hendry County Sheriff's Office**
  - **Hernando County Sheriff's Office**
  - **High Springs Police Department**
  - **Madison County Sheriff's Office**
  - **Highland Beach Police Department**
  - **Manatee County Sheriff's Office**
  - **Highlands County Sheriff's Office**
  - **Hillsborough County Sheriff's Office**
  - **Marion County Sheriff's Office**
  - **Holly Hill Police Department**
  - **Martin County Sheriff's Office**
  - **Holmes Beach Police Department**
  - **Holmes County Sheriff's Office**
  - **Indian Harbour Beach Police Department**
  - **Miami Dade Corrections and Rehabilitation**
  - **Indian River County Sheriff's Office**
  - **Monroe County Sheriff's Office**
  - **Indian River Shores Department of Public Safety**
  - **Indian Shores Police Department**
  - **Nassau County Sheriff's Office**
  - **Indiatlantic Police Department**
  - **Jackson County Sheriff's Office**
  - **Jacksonville Sheriff's Office**
  - **Jefferson County Sheriff's Office**
  - **Juno Beach Police Department**
  - **Jupiter Inlet Colony Police Department**
  - **Jupiter Island Department of Public Safety**
  - **Jupiter Police Department**
  - **Okaloosa County Sheriff's Office**
  - **Okeechobee County Sheriff's Office**
  - **Kenneth City Police Department**
  - **Orange County Corrections Department**
  - **Key Colony Beach Police Department**
  - **Key West Police Department**
  - **Osceola County Corrections Department**
  - **Kissimmee Police Department**
  - **Lady Lake Police Department**
  - **Palm Beach County Sheriff's Office**
  - **Lafayette County Sheriff's Office**
  - **Lake City Police Department**
  - **Lake Clark Shores Police Department**
  - **Lake County Sheriff's Office**
  - **Pasco County Board of County Commissioners**
  - **Lake Placid Police Department**
  - **Lakeland Police Department**
  - **Pinellas County Sheriff's Office**
  - **Lantana Police Department**
  - **Lee County Sheriff's Office**
  - **Polk County Sheriff's Office**
  - **Leon County Sheriff's Office**
  - **Levy County Sheriff's Office**
  - **Liberty County Sheriff's Office**
  - **Lighthouse Point Police Department**
  - **Putnam County Sheriff's Office**
  - **Live Oak Police Department**
  - **Longboat Key Police Department**
  - **Longwood Police Department**
  - **Santa Rosa County Sheriff's Office**
  - **Lynn Haven Police Department**
  - **Sarasota County Sheriff's Office**
  - **Madison County Sheriff's Office**
  - **Manatee County Sheriff's Office**
  - **Seminole County Sheriff's Office**
  - **Marco Island Police Department**
  - **Marianna Police Department**
  - **Marion County Sheriff's Office**
  - **Martin County Sheriff's Office**
  - **St. Johns County Sheriff's Office**
  - **St. Lucie County Sheriff's Office**
  - **Melbourne Beach Police Department**
  - **Melbourne International Airport Police Department**
  - **Melbourne Police Department**
  - **Sumter County Sheriff's Office**
  - **Miami Dade Sheriff's Office**
  - **Suwannee County Sheriff's Office**
  - **Monroe County Sheriff's Office**
  - **Naples Police Department**
  - **Nassau County Sheriff's Office**
  - **Taylor County Sheriff's Office**
  - **New College of Florida Police Department**
  - **New Port Richey Police Department**
  - **New Smyrna Beach Police Department**
  - **Union County Sheriff's Office**
  - **North Bay Village Police Department**
  - **North Port Police Department**
  - **Northwest Florida State College Police Department**
  - **Volusia County Division of Corrections**
  - **Oakland Police Department**
  - **Wakulla County Sheriff's Office**
  - **Ocala Police Department**
  - **Walton County Sheriff's Office**
  - **Ocean Ridge Police Department**
  - **Washington County Sheriff's Office**
  - **Ocoee Police Department**
  - **Okaloosa County Sheriff's Office**
  - **Okeechobee County Sheriff's Office**
  - **Okeechobee Police Department**
  - **Orange City Police Department**
  - **Orange County Sheriff's Office**
  - **Orlando Police Department**
  - **Ormond Beach Police Department**
  - **Osceola County Sheriff's Office**
  - **Oviedo Police Department**
  - **Palm Beach County Sheriff's Office**
  - **Palm Beach Gardens Police Department**
  - **Panama City Beach Police Department**
  - **Panama City Police Department**
  - **Pasco County Sheriff's Office**
  - **Pembroke Park Police Department**
  - **Pembroke Pines Police Department**
  - **Pinellas County Sheriff's Office**
  - **Pinellas Park Police Department**
  - **Polk County Sheriff's Office**
  - **Ponce Inlet Police Department**
  - **Port Orange Police Department**
  - **Punta Gorda Police Department**
  - **Putnam County Sheriff's Office**
  - **Riviera Beach Police Department**
  - **Sanford Airport Police Department**
  - **Sanibel Police Department**
  - **Santa Rosa County Sheriff's Office**
  - **Sarasota County Sheriff's Office**
  - **Sarasota Police Department**
  - **Sebastian Police Department**
  - **Seminole County Sheriff's Office**
  - **Sewall's Point Police Department**
  - **South Daytona Police Department**
  - **Springfield Police Department**
  - **St. Augustine Beach Police Department**
  - **St. Augustine Police Department**
  - **St. Cloud Police Department**
  - **St. Johns County Sheriff's Office**
  - **St. Lucie County Sheriff's Office**
  - **St. Petersburg Police Department**
  - **Stuart Police Department**
  - **Sumter County Sheriff's Office**
  - **Sunny Isles Police Department**
  - **Suwannee County Sheriff's Office**
  - **Sweetwater Police Department**
  - **Tallahassee Police Department**
  - **Tallahassee State College Police Department**
  - **Tampa Police Department**
  - **Tarpon Springs Police Department**
  - **Tavares Police Department**
  - **Taylor County Sheriff's Office**
  - **Tequesta Police Department**
  - **Town of Palm Beach Police Department**
  - **Treasure Island Police Department**
  - **Union County Sheriff's Office**
  - **University of Central Florida Board of Trustees**
  - **University of Florida Police Department**
  - **University of West Florida Police Department**
  - **Venice Police Department**
  - **Vero Beach Police Department**
  - **Volusia County Sheriff's Office**
  - **Wakulla County Sheriff's Office**
  - **Walton County Sheriff's Office**
  - **Washington County Sheriff's Office**
  - **West Melbourne Police Department**
  - **West Miami Police Department**
  - **Winter Garden Police Department**

### State: GEORGIA
  - **Euharlee Police Department**
  - **Georgia Department of Public Safety**
  - **Bibb County Sheriff's Office**
  - **Burke County Sheriff's Office**
  - **Columbia County Sheriff's Office**
  - **Dade County Sheriff's Office**
  - **Decatur County Sheriff's Office**
  - **Floyd County Sheriff's Office**
  - **Forsyth County Sheriff's Office**
  - **Georgia Department of Corrections**
  - **Glynn County Sheriff's Office**
  - **Hall County Sheriff's Office**
  - **Lumpkin County Sheriff's Office**
  - **Madison County Sheriff's Office**
  - **Monroe County Sheriff's Office**
  - **Morgan County Sheriff's Office**
  - **Oconee County Sheriff's Office**
  - **Pierce County Sheriff's Office**
  - **Polk County Sheriff's Office**
  - **Tift County Sheriff's Office**
  - **Tift County Sheriff's Office**
  - **Walker County Sheriff's Office**
  - **Whitfield County Sheriff's Office**

### State: IDAHO
  - **Gooding County Sheriff's Office**
  - **Owyhee County Sheriff's Office**
  - **Power County Sheriff’s Office**
  - **Owyhee County Sheriff's Office**

### State: INDIANA
  - **Green Forks Police Department**
  - **Hamilton County Sheriff's Office**
  - **Jasper County Sheriff's Office**
  - **Noble County Sheriff's Office**

### State: IOWA
  - **Iowa Department of Public Safety**

### State: KANSAS
  - **Kansas Bureau of Investigation**
  - **Cowley County Sheriff's Office**
  - **Finney County Sheriff’s Office**
  - **Jackson County Sheriff’s Office**
  - **Reno County Sheriff's office**
  - **Rice County Sheriff's Office**

### State: KENTUCKY
  - **Bracken County Sheriff's Office**
  - **Daviess County Sheriff's Office**
  - **Grayson County Sheriff’s Office**
  - **Heritage Creek Police Department**
  - **Lyon County Sheriff's Office**
  - **Marshall County Sheriff's Office**
  - **Bullitt County Detention Center**
  - **Daviess County Sheriff's Office**
  - **Grayson County Detention Center**
  - **Grayson County Detention Center**
  - **Kenton County Sheriff's Office**
  - **Kenton County Sheriff's Office**
  - **Oldham County Detention Center**
  - **Oldham County Detention Center**
  - **Union County Sheriff's Office**

### State: LOUISIANA
  - **Beauregard Parish Sheriff's Office**
  - **Bossier Parish Sheriff's Office**
  - **Kenner Police Department**

### State: MAINE
  - **Wells Police Department**

### State: MARYLAND
  - **Carroll County Sheriff’s Office**
  - **Cecil County Sheriff's Office**
  - **Frederick County Sheriff's Office**
  - **Garrett County Sheriff's Office**
  - **Harford County Sheriff's Office**
  - **St. Mary's County Sheriff's Office**
  - **Washington County Sheriff's Office**

### State: MASSACHUSETTS
  - **Massachusetts Department of Corrections**

### State: MICHIGAN
  - **Berrian County Sheriff's Office**
  - **Calhoun County Sheriff's Office**
  - **Jackson County Sheriff's Office**
  - **Taylor Police Department**

### State: MINNESOTA
  - **Cass County Sheriff's Office**
  - **Crow Wing County Sheriff's Office**
  - **Itasca County Sheriff's Office**
  - **Crow Wing County Sheriff's Office **
  - **Freeborn County Sheriff's Office**
  - **Jackson County Sheriff's Office**
  - **Jackson County Sheriff's Office**

### State: MISSISSIPPI
  - **Mississippi Attorney General's Office**

### State: MISSOURI
  - **Missouri Highway Patrol**
  - **Christian County Sheriff's Office**
  - **Christian County Sheriff's Office**
  - **Saint Mary Police Department**

### State: MONTANA
  - **Montana Department of Justice**
  - **Flathead County Sheriff's Department**
  - **Gallatin County Sheriff's Office**

### State: NEBRASKA
  - **Dakota County Sheriff's Office**
  - **Wheeler County Sheriff's Office**

### State: NEVADA
  - **Douglas County Sheriff's Office**
  - **Mineral County Sheriff's Office**

### State: NEW HAMPSHIRE
  - **Belknap County Sheriff's Office**
  - **Candia Police Department**
  - **Colebrook Police Department**
  - **Gorham Police Department**
  - **Grafton County Sheriff's Office**
  - **Hillsborough County Sheriff's Office**
  - **New Hampshire State Police**
  - **Ossipee Police Department**
  - **Pittsburgh Police Department**
  - **Rockingham County Sheriff's Office **
  - **Troy Police Department**

### State: NEW MEXICO
  - **Curry County Sheriff's Office**

### State: NEW YORK
  - **Nassau County Police Department**
  - **Niagara County Sheriff's Office**
  - **Broome County Sheriff's Office**
  - **Nassau County Sheriff's Office**
  - **Niagara County Sheriff's Office**
  - **Rensselaer County Sheriff's Office**

### State: NORTH CAROLINA
  - **Alamance County Sheriff's Office**
  - **Albemarle District Jail**
  - **Avery County Sheriff's Office**
  - **Brunswick County Sheriff's Office**
  - **Cabarrus County Sheriff's Office**
  - **Caldwell County Sheriff's Office**
  - **Carteret County Sheriff's Office**
  - **Cherokee County Sheriff's Office**
  - **Cleveland County Sheriff's Office**
  - **Columbus County Sheriff's Office**
  - **Craven County Sheriff's Office**
  - **Duplin County Sheriff's Office**
  - **Gaston County Sheriff's Office**
  - **Henderson County Sheriff's Office**
  - **Lincoln County Sheriff's Office**
  - **Nash County Sheriff's Office**
  - **Onslow County Sheriff's Office**
  - **Randolph County Sheriff's Office**
  - **Rockingham County Sheriff's Office**
  - **Union County Sheriff's Office**
  - **Yancey County Sheriff's Office**

### State: NORTH DAKOTA
  - **Dickinson Police Department**
  - **Dunn County Sheriff's Office**
  - **Eddy County Sheriff's Office**
  - **McKenzie County Sheriff's Office**
  - **Dunn County Sheriff's Office**

### State: OHIO
  - **Butler County Sheriff's Office**
  - **Portage County Sheriff's Office**
  - **Seneca County Sheriff's Office**
  - **Butler County Sheriff's Office**
  - **Portage County Sheriff's Office**
  - **Seneca County Sheriff's Office**

### State: OKLAHOMA
  - **Eufaula Police Department**
  - **Fletcher Police Department**
  - **Oklahoma Bureau of Investigation**
  - **Oklahoma Bureau of Narcotics**
  - **Oklahoma Department of Public Safety**
  - **Blaine County Sheriff's Office**
  - **Canadian County Sheriff's Office**
  - **Lincoln County Sheriff's Office**
  - **Logan County Sheriff's Office**
  - **Muskogee County Sheriff's Office**
  - **Okmulgee County Criminal Justice Authority**
  - **Okmulgee County Criminal Justice Authority**
  - **Tulsa County Sheriff's Office**
  - **Sterling Police Department**
  - **Vinita Police Department**

### State: PENNSYLVANIA
  - **Bucks County Sheriff's Office**
  - **Damascus Township Constable**
  - **Derry Township Constable's Office**
  - **Franklin County Sheriffs Office**
  - **Lancaster County Sheriff's Office**
  - **Lower Burrell Fourth Ward Constable**
  - **Northwest Regional Police Department**
  - **Preston Township Constable's Office**
  - **Sewickley Township Constable's Office**
  - **Bradford County Sheriff's Office**
  - **Franklin County Sheriffs Office**

### State: SOUTH CAROLINA
  - **Berkeley County Sheriff's Office**
  - **Kershaw County Sheriff's Office**
  - **Pickens County Sheriff's Office**
  - **South Carolina Law Enforcement Division**
  - **Berkeley County Sheriff's Office**
  - **Charleston County Sheriff's Office**
  - **Chester County Sheriff's Office**
  - **Greenville County Sheriff's Office**
  - **Horry County Sheriff's Office**
  - **Lancaster County Sheriff's Office**
  - **Lexington County Sheriff's Office**
  - **Oconee County Sheriff's Office**
  - **Spartanburg County Sheriff's Office**
  - **York County Sheriff's Office**

### State: SOUTH DAKOTA
  - **Hughes County Sheriff's Office**
  - **Minnehaha County Sheriff's Office**

### State: STATE
  - **LAW ENFORCEMENT AGENCY**

### State: TENNESSEE
  - **Giles County Sheriff's Office**
  - **Greene County Sheriff’s Office**
  - **Hamilton County Sheriff's Office**
  - **Knox County Sheriff’s Office**
  - **Putnam County Sheriff's Office**
  - **Sumner County Sheriff's Office**
  - **Tennessee Department of Safety and Homeland Security / THP**

### State: TEXAS
  - **Atascosa County Sheriff's Office**
  - **Calhoun County Sheriff's Office**
  - **Coke County Sheriff's Office**
  - **Falls County Sheriff's Office**
  - **Goliad County Sheriff's Office**
  - **Hamilton County Sheriff's Office **
  - **Jim Wells County Sheriff's Office**
  - **Kerr County Sheriff's Office**
  - **Kinney County Sheriff's Office**
  - **Medina County Sheriff's Office**
  - **Nixon Police Department**
  - **Panola County Sheriff's Office**
  - **Smith County Sheriff’s Office**
  - **Sutton County Sheriff's Office**
  - **Aransas County Sheriff's Office**
  - **Austin County Sheriff's Office**
  - **Bee County Sheriff's Office**
  - **Burleson County Sheriff's Office**
  - **Burnet County Sheriff's Office**
  - **Calhoun County Sheriff’s Office**
  - **Calhoun County Sheriff's Office**
  - **Chambers County Sheriff’s Office**
  - **Deaf Smith County Sheriff's Office**
  - **DeWitt County Sheriff’s Office**
  - **DeWitt County Sheriff’s Office**
  - **Ellis County Sheriff's Office**
  - **Fayette County Sheriff's Office**
  - **Galveston County Sheriff’s Office**
  - **Galveston County Sheriff's Office**
  - **Goliad County Sheriff’s Office**
  - **Goliad County Sheriff's Office**
  - **Gonzales County Sheriff's Office**
  - **Grayson County Sheriff’s Office**
  - **Gregg County Sheriff's Office**
  - **Harrison County Sheriff's Office**
  - **Hill County Sheriff's Office**
  - **Hood County Sheriff's Office**
  - **Houston County Sheriff's Office**
  - **Jackson County Sheriff's Office**
  - **Jackson County Sheriff's Office **
  - **Jim Wells County Sheriff's Office**
  - **Jim Wells County Sheriff's Office**
  - **Kendall County Sheriff's Office**
  - **Texas National Guard**
  - **Kerr County Sheriff's Office**
  - **Kerr County Sheriff's Office**
  - **Texas Office of the Attorney General**
  - **Kleberg County Sheriff's Office**
  - **Lavaca County Sheriff’s Office**
  - **Lavaca County Sheriff's Office**
  - **Live Oak County Sheriff's Office **
  - **Lubbock County Sheriff's Office**
  - **Matagorda County Sheriff's Office**
  - **McMullen County Sheriff's Office**
  - **Titus County Sheriff's Office**
  - **Montgomery County Sheriff’s Office**
  - **Nixon Police Department**
  - **Nueces County Sheriff's Office**
  - **Orange County Sheriff's Office**
  - **Panola County Sheriff's Office**
  - **Parker County Sheriff's Office**
  - **Polk County Sheriff's Office**
  - **Potter County Sheriff's Office**
  - **Randall County Sheriff's Office**
  - **Refugio County Sheriff’s Office**
  - **Refugio County Sheriff’s Office**
  - **Rockwall County Sheriff's Office**
  - **Rusk County Sheriff's Office **
  - **San Patricio County Sheriff’s Office**
  - **Schleicher County Sheriff's Office**
  - **Smith County Sheriff’s Office**
  - **Sutton County Sheriff's Office**
  - **Tarrant County Sheriff’s Office**
  - **Terrell County Sheriff's Office**
  - **Terrell County Sheriff's Office**
  - **Titus County Sheriff's Office**
  - **Victoria County Sheriff’s Office**
  - **Victoria County Sheriff’s Office**
  - **Walker County Sheriff’s Department**
  - **Walker County Sheriff's Office**
  - **Waller County Sheriff’s Office**
  - **Wharton County Sheriff’s Office**
  - **Wharton County Sheriff's Office**
  - **Wichita County Sheriff's Office**
  - **Winkler County Sheriff's Office**
  - **Winkler County Sheriff's Office**
  - **Winkler County Sheriff's Office**

### State: UTAH
  - **Utah Department of Corrections**
  - **Washington County Sheriff's Office**
  - **Washington County Sheriff's Office**

### State: VIRGINIA
  - **Appomattox County Sheriff's Office**
  - **Bedford County Sheriff's Office**
  - **Buckingham County Sheriff's Office**
  - **Campbell County Sheriff's Office**
  - **Craig County Sheriff's Office**
  - **Franklin County Sheriff's Office**
  - **Grayson County Sheriff's Office**
  - **Greene County Sheriff's Office**
  - **Mecklenburg County Sheriff's Office**
  - **Shenandoah County Sheriff's Office**
  - **Smyth County Sheriff's Office **
  - **Virginia Department of State Police**
  - **Loudoun County Sheriff's Office**
  - **Southwest Virginia Regional Jail Authority**
  - **Virginia Department of Corrections**

### State: WEST VIRGINIA
  - **Wood County Sheriff's Office**

### State: WISCONSIN
  - **Brown County Sheriff's Office**
  - **Fond du Lac County Sheriff's Office**
  - **Manitowoc County Sheriff's Office**
  - **Marquette County Sheriff's Office**
  - **Outagamie County Sheriff's Office**
  - **Sheboygan County Sheriff's Office**
  - **Washington County Sheriff's Office**
  - **Waukesha County Sheriff's Office**
  - **Waukesha County Sheriff's Office**
  - **Waupaca County Sheriff's Office**
  - **Waushara County Sheriff's Office**
  - **Winnebago County Sheriff's Office**
  - **Wood County Sheriff's Office**

### State: WYOMING
  - **Natrona County Sheriff's Office**
  - **Sweetwater County Sheriff's Office**
  - **Campbell County Sheriff's Office**
  - **Laramie County Sheriff’s Office**
  - **Sweetwater County Sheriff's Office**
  - **Sweetwater County Sheriff's Office**
