# colleges-api
API to get all the colleges in India

Here we have used the data from https://data.gov.in/catalog/list-colleges-aishe-survey 

## Requirements

* Python



### Listing total number of colleges by university name

**GET:** */get/university/Goa*

**RESPONSE :**

```json
[
    {
        "Total Colleges in university": 65
    },
    [
        {
            "college_name": "AGNEL INSTITUTE OF TECHNOLOGY AND DESIGN, ASSAGAO, BARDEZ (Id: C-46329)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Carmel College of Arts Science & Commerce for Women (Id: C-33103)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Centre for Latin American Studies (Id: C-30837)",
            "college_type": "PG Center / Off-Campus Center",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Centre for Women's Studies (Id: C-30871)",
            "college_type": "PG Center / Off-Campus Center",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Cuncolim Educational Societys College of Arts & Commerce Cuncolim (Id: C-30867)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Dempo Charities Trust Dhempe College of Arts & Science Miramar (Id: C-30842)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Dempo Charities Trusts S.S. Dempo College of Commerce & Economics Altinho (Id: C-30828)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Devi Sharvani Education Societys V.M. Salgaocar College of Law Miramar Panaji (Id: C-30825)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Directorate of Archives and Archaeology (Id: C-30840)",
            "college_type": "Recognized Center",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Dnyan Prabodhini Mandals Shree Mallikarjun College of Arts & Commerce Delem Canacona (Id: C-30865)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Dnyanprassarak Mandals College of Arts Sou. Sheela Premanand Vaidya College of Science & VNS Bandekar College of Commerce Assagao (Id: C-30843)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "DON BOSCO COLLEGE OF ENGINEERING, FATORDA, MARGAO (Id: C-46324)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Fisheries Survey of India (Id: C-30870)",
            "college_type": "Recognized Center",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Fr. Agnel College of Arts & Commerce Pilar (Id: C-30863)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Goa College of Architecture Altinho Panaji (Id: C-30832)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Goa College of Art Altinho Panaji (Id: C-30835)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Goa College of Home Science Campal Panaji (Id: C-30824)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "GOA COLLEGE OF HOSPITALITY AND CULINARY EDUCATION, CIDADE-DE-GOA (Id: C-46325)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Goa College of Music Altinho Panaji (Id: C-30869)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Goa College of Pharmacy Panaji (Id: C-30858)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Goa Dental College & Hospital Bambolim (Id: C-30817)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Goa Medical College Bambolim (Id: C-30851)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Goa Salesian Societys Don Bosco College Panaji (Id: C-30823)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Goa Vidyaprasarak Mandal's Dr. Dada Vaidya College of Education, Ponda (Id: C-35084)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Goa Vidyaprasarak Mandals Gopal Govind Poy Raiturcar College of Commerce and Economics Farmagudi Ponda (Id: C-30818)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Govt. College of Arts & Commerce Virnoda Pernem (Id: C-30862)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Govt.College of Arts Science & Commerce Khandola (Id: C-35081)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Govt.College of Arts Science & Commerce Quepem (Id: C-30845)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Govt.College of Arts Science & Commerce Sanquelim (Id: C-30847)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Govt. College of Commerce Borda Margao (Id: C-30848)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Govt. of Goa College of Engineering, Goa, Farmagudi, Ponda (Id: C-30821)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Indian Naval Academy Ezhimala (Id: C-30854)",
            "college_type": "Affiliated College",
            "district": "Kannur",
            "state": "Kerala",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "INS Hamla Marve Malad (Id: C-30827)",
            "college_type": "Affiliated College",
            "district": "Mumbai",
            "state": "Maharashtra",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Institute of Nursing Education Bambolim (Id: C-30836)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Institute of Psychiatry & Human Behaviour Bambolim (Id: C-30855)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Malaria Research Centre (Id: C-30839)",
            "college_type": "Recognized Center",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Murgaon Education Societys College of Arts & Commerce Zuarinagar (Id: C-30864)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "National Centre for Antarctic & Ocean Research (Id: C-30853)",
            "college_type": "Recognized Center",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "National Hydrographic School C/o Headquarters Vasco-da-Gama (Id: C-30849)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "National Institute of Malaria Research (Id: C-30831)",
            "college_type": "Recognized Center",
            "district": "North",
            "state": "Delhi",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "National Institute of Oceanography (Id: C-30826)",
            "college_type": "Recognized Center",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Nirmala Institute of Education Altinho Panaji (Id: C-30850)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Padre Conceicao College of Engineering Agnel Ashram Verna (Id: C-30819)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Parvatibai Chowgule College of Arts & Science (Id: C-30820)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Ponda Education Societys College of Education Farmagudi Ponda (Id: C-30868)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Ponda Education Society Shri Ravi S Naik College of Arts & Science (Id: C-30860)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Ponda Education Society's Rajaram and Tarabai Bandekar College of Pharmacy, Farmagudi, Ponda (Id: C-35083)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Rosary College of Commerce & Arts Navelim (Id: C-30852)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Saraswat Vidyalayas Sridora Caculo College of Commerce & Management Studies Mapusa (Id: C-30834)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Shivgram Education Societys Shri Kamaxidevi Homoeopathic Medical College & Hospital Shiroda (Id: C-30856)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Shree Bharateeya Sanskriti Prabodhinis Gomantak Ayurveda Mahavidyalaya & Research Centre Shiroda (Id: C-30874)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Shree Rayeshwar Institute of Engineering & Information Technology Shiroda (Id: C-44947)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "St Xaviers College of Arts Science & Commerce Mapusa (Id: C-30875)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "SWAMI VIVEKANAND VIDYA PRASARAK MANDALS COLLEGE OF COMMERCE, (Id: C-46327)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Syngenta Research & Technology Centre (Id: C-30866)",
            "college_type": "Recognized Center",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Thomas Stephen's Konkani Kendra (Id: C-30857)",
            "college_type": "Recognized Center",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Victor Medical & Research Foundation College of Nursing C/o Apollo Victor Hospital Malbhat Margao (Id: C-30844)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "VIDYA PRABODHINI COLLEGE OF COMMERCE, EDUCATION, COMPUTER AND MANAGEMENT, VIDYANAGAR, ALTO PORVORIM (Id: C-46328)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Vidya Vikas Mandals Govind Ramnath Kare College of Law Margao (Id: C-30838)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Vidya Vikas Mandals H.M.N. Gaunekar Institute of Management Training & Research Shre Damodar College Complex Margao (Id: C-30822)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Vidya Vikas Mandals Shree Damodar College of Commerce & Economics Margao (Id: C-30846)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "VIKAS PARISHAD MANDRE COLLEGE OF COMMERCE AND ECONOMICS, MANDHLAMANJ, MANDREM (Id: C-46326)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Vrundavan Institute of Nursing Education & College of Nursing Colvale Bardez (Id: C-30872)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Xavier Centre of Historical Research (Id: C-30833)",
            "college_type": "Recognized Center",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Zantye Brothers Educational Foundations Narayan Zantye College of Commerce Bicholim (Id: C-30873)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        }
    ]
]
```

---------------------------------------

### Searching a College by state

**POST:** */get/state/Sikkim*

**REQUEST :**
```
POST /colleges/search HTTP/1.1
HOST: localhost:5000
 ```

**RESPONSE :**

```json
[
    {
        "Total Colleges in state": 20
    },
    [
        {
            "college_name": "College of Agricultural Engineering and Post Harvest Technology, Ranipool, Gangtok (Id: C-26829)",
            "college_type": "Constituent / University College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Central Agricultural University, Imphal (Id: U-0336)"
        },
        {
            "college_name": "School of Basic & Applied Sciences (SBAS) (Id: C-8628)",
            "college_type": "Constituent / University College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Sikkim Manipal University, Gangtok (Id: U-0431)"
        },
        {
            "college_name": "Sikkim Manipal College of Nursing (SMCON) (Id: C-8624)",
            "college_type": "Constituent / University College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Sikkim Manipal University, Gangtok (Id: U-0431)"
        },
        {
            "college_name": "Sikkim Manipal College of Physiotherapy (SMCOP) (Id: C-8626)",
            "college_type": "Constituent / University College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Sikkim Manipal University, Gangtok (Id: U-0431)"
        },
        {
            "college_name": "Sikkim Manipal Institute of Medical Sciences (SMIMS) (Id: C-8625)",
            "college_type": "Constituent / University College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Sikkim Manipal University, Gangtok (Id: U-0431)"
        },
        {
            "college_name": "Sikkim Manipal Institute of Technology (SMIT) (Id: C-8627)",
            "college_type": "Constituent / University College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Sikkim Manipal University, Gangtok (Id: U-0431)"
        },
        {
            "college_name": "Damber Singh College, 6th mile, Samdur (Id: C-6599)",
            "college_type": "Affiliated College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Sikkim University, Gangtok (Id: U-0430)"
        },
        {
            "college_name": "Government College Rhenock, Rungdung (Id: C-6598)",
            "college_type": "Affiliated College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Sikkim University, Gangtok (Id: U-0430)"
        },
        {
            "college_name": "Harkamaya College of Education, 6th mile, Samdur (Id: C-6595)",
            "college_type": "Affiliated College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Sikkim University, Gangtok (Id: U-0430)"
        },
        {
            "college_name": "Himalayan Pharmacy Institute, Majhitar (Id: C-6594)",
            "college_type": "Affiliated College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Sikkim University, Gangtok (Id: U-0430)"
        },
        {
            "college_name": "Loyola College of Education, Namchi (Id: C-6596)",
            "college_type": "Affiliated College",
            "district": "South District",
            "state": "Sikkim",
            "university": "Sikkim University, Gangtok (Id: U-0430)"
        },
        {
            "college_name": "Namchi Government College, Kamrang (Id: C-6600)",
            "college_type": "Affiliated College",
            "district": "South District",
            "state": "Sikkim",
            "university": "Sikkim University, Gangtok (Id: U-0430)"
        },
        {
            "college_name": "Pakim Palatine College, Pakyong (Id: C-6597)",
            "college_type": "Affiliated College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Sikkim University, Gangtok (Id: U-0430)"
        },
        {
            "college_name": "Sikkim Government B.Ed College, Soreng (Id: C-6602)",
            "college_type": "Affiliated College",
            "district": "West District",
            "state": "Sikkim",
            "university": "Sikkim University, Gangtok (Id: U-0430)"
        },
        {
            "college_name": "SIKKIM GOVERNMENT COLLEGE, GYALSHING (Id: C-47497)",
            "college_type": "Affiliated College",
            "district": "West District",
            "state": "Sikkim",
            "university": "Sikkim University, Gangtok (Id: U-0430)"
        },
        {
            "college_name": "Sikkim Government College,Tadong (Id: C-6603)",
            "college_type": "Affiliated College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Sikkim University, Gangtok (Id: U-0430)"
        },
        {
            "college_name": "Sikkim Government Law College,Burtuk (Id: C-6601)",
            "college_type": "Affiliated College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Sikkim University, Gangtok (Id: U-0430)"
        },
        {
            "college_name": "VINAYAKA MISSIONS SIKKIM COLLEGE OF ARTS AND SCIENCES (Id: C-47716)",
            "college_type": "Constituent / University College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Vinayaka Missions Sikkim University, Tadong (Id: U-0433)"
        },
        {
            "college_name": "VINAYAKA MISSIONS SIKKIM COLLEGE OF NURSING (Id: C-47717)",
            "college_type": "Constituent / University College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Vinayaka Missions Sikkim University, Tadong (Id: U-0433)"
        },
        {
            "college_name": "VINAYAKA MISSIONS SIKKIM COLLEGE OF PHARMACEUTICAL SCIENCES (Id: C-47718)",
            "college_type": "Constituent / University College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Vinayaka Missions Sikkim University, Tadong (Id: U-0433)"
        }
    ]
]
```

---------------------------------------

### Getting colleges in a District

**GET:** */get/district/Jalgaon*

**Headers:** 

State - State to search

#### Example

**REQUEST :**
```
HOST: localhost:5000
State: Jalgaon
 ```

**RESPONSE :**

```json
[
    {
        "Total Colleges in district": 107
    },
    [
        {
            "college_name": "Chaitanya Ayurved Mahavidyalya, Sakegaon, Tal-Bhusawal (Id: C-13734)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Maharashtra University of Health Sciences, Nashik (Id: U-0313)"
        },
        {
            "college_name": "Dr. Ulhas Patil College of Physiotherapy, Jalgaon (Id: C-14044)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Maharashtra University of Health Sciences, Nashik (Id: U-0313)"
        },
        {
            "college_name": "Godavari Foundations Dr. Ulhas Patil Medical College & Hospital, Jalgaon Khurd, Tal. & Dist. Jalgaon (Id: C-13807)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Maharashtra University of Health Sciences, Nashik (Id: U-0313)"
        },
        {
            "college_name": "Godavari Foundations Godavari College of Nursing (P.B.B.Sc.), Jalgaon (Id: C-13919)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Maharashtra University of Health Sciences, Nashik (Id: U-0313)"
        },
        {
            "college_name": "Godavari Foundations Nursing College, Jalgaon (Id: C-13802)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Maharashtra University of Health Sciences, Nashik (Id: U-0313)"
        },
        {
            "college_name": "Iqra Unani Medical College, Jalgaon (Id: C-14042)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Maharashtra University of Health Sciences, Nashik (Id: U-0313)"
        },
        {
            "college_name": "KDMGs Ayurved Medical College, Chalisgaon (Id: C-13934)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Maharashtra University of Health Sciences, Nashik (Id: U-0313)"
        },
        {
            "college_name": "Shri Chamundamata Homoeopathy College, Jalgaon (Id: C-13861)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Maharashtra University of Health Sciences, Nashik (Id: U-0313)"
        },
        {
            "college_name": "100001-KCES'S MOOLJEE JAITHA COLLEGE, JALGAON. (Id: C-8888)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100002-JDMVP CO-OP S'S ARTS, COMMERCE & SCIENCE COLLEGE, JALGAON. (Id: C-8913)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100003-EU'S DR. ANNASAHEB G.D.BENDALE MAHILA MAHAVIDYALAYA, JALGAON. (Id: C-8979)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100004-KCES'S COLLEGE OF EDUCATION, JALGAON. (Id: C-8922)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100005-KCES'S S.S.MANIYAR LAW COLLEGE, JALGAON. (Id: C-9030)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100006-KRES'S ADV.SITARAM (BABANBHAU) A.BAHETI ARTS,COMMERCE&SCIENCE COLLEGE, JALGAON (Id: C-9025)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100007-SSBT'S COLLEGE OF ENGINEERING & TECHNOLOGY, BAMBHORI. (Id: C-8977)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100008-SES'S COLLEGE OF PHYSICAL EDUCATION, JALGAON. (Id: C-8876)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100009-IES'S H.J.THIM COLLEGE OF ARTS&SCIENCE, MEHRUN. (Id: C-8940)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100010-KCES'S INSTITUTE OF MANAGEMENT & RESEARCH, JALGAON. (Id: C-9027)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100043-IES'S IQRA COLLEGE OF EDUCATION, MEHRUN. (Id: C-8833)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100054-GOVERNMENT COLLEGE OF ENGINEERING, JALGAON. (Id: C-8946)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100055-DNCVP'S COLLEGE OF SOCIAL WORK, JALGAON. (Id: C-8918)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100060-DNCVP'S CHETANA INSTITUTE OF COMPUTER MANAGEMENT & RESEARCH, JALGAON (Id: C-8812)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100061-SE&CM'S SHRI GULABRAO DEOKAR COLLEGE OF ENGINEERING, JALGAON. (Id: C-8860)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100062-K.A.K.P. SANSHTA'S COMMERCE & SCIENCE COLLEGE, JALGAON (Id: C-8862)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100063-GF'S GODAVARI COLLEGE OF ENGINEERING, JALGAON (Id: C-8836)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100066-DNCVP'S ARTS & SCIENCE COLLEGE, JALGAON (Id: C-8907)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100074-GODAVARI FOUNDATION'S DR.ULHAS PATIL COLLEGE OF SCIENCE&COMMERCE,JALGAON. (Id: C-8943)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100081-GODAVARI FOUNDATION'S GODAVARI INSTITUTE OF MANAGEMENT & RESEARCH JALGAON (Id: C-8905)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100084-KCES'S COLLEGE OF ENGINEERING & INFORMATION TECHNOLOGY, JALGAON (Id: C-8815)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100089-GFS'S GODAVARI COLLEGE OF MUSIC & FINE ARTS,JALGAON (Id: C-9023)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100090-GFS'S DR.ULHAS PATIL LAW COLLEGE, JALGAON (Id: C-8899)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100092-LATE B.R.KOLHE SS'S LALIT KALA MAHAVIDYALAYA, JALGAON. (Id: C-8903)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100094-COLLEGE OF ARCHITECTURE, JALGAON (Id: C-10236)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100098-JZMDS'S COLLEGE OF PHARMACY,MAMURABAD,JALGAON (Id: C-8852)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100099-KCES'S EKLAVYA COLLEGE OF PHYSICAL EDUCATION, JALGAON. (Id: C-9000)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100100-G.H. RAISONI INSTITUTE OF ENGINEERING & MANAGEMENT, JALGAON. (Id: C-8831)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100101-GHREFS'S G.H. RAISONI INSTITUTE OF INFORMATION TECHNOLOGY, JALGAON. (Id: C-8991)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100103-SES'S COLLEGE OF EDUCATION, JALGAON. (Id: C-8998)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100105-JAI DURGA BHAVANI KRIDA MANDAL'S OM SAI COLLEGE OF EDUCATION, SHIRSOLI (Id: C-8864)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100110-SMBKMP'S SHRI.CHHATRAPATI RAJE SAMBHAJI COLLEGE OF EDUCATION, JALGAON (Id: C-9013)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100112-EKES'S RAOSAHEB RUPCHAND SENIOR COLLEGE,JALGAON (Id: C-8813)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "100113-KCES'S POST GRADUATE COLLEGE OF SCIENCE TECH.& RESEARCH, JALGAON. (Id: C-8877)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "110012-TES'S BHUSAWAL ARTS,SCIENCE & P.O.NAHATA COMMERCE COLLEGE, BHUSAWAL. (Id: C-8915)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "110013-SSVPM'S SMT.P.K.KOTECHA MAHILA MAHAVIDYALAYA, BHUSAWAL. (Id: C-9032)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "110015-JDMVP CO-OP S'S ARTS,COMMERCE & SCIENCE COLLEGE, VARANGAON. (Id: C-8834)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "110016-BSCES'S ARTS & COMMERCE COLLEGE, BODVAD. (Id: C-9017)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "110044-TES'S INSTITUTE OF MANAGEMENT & CAREER DEVELOPMENT, BHUSAWAL. (Id: C-8967)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "110050-THE BHUSAWAL PEOPLES CHARI.SANSTHA'S DADASAHEB DEVIDAS N.BHOLE COLLEGE,BHUSAWAL. (Id: C-8994)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "110059-HINDI SEVA MANDAL'S SHRI.SANT GADGE BABA COLLEGE OF ENGINEERING & TECHNOLOGY, BHUSAWAL (Id: C-8830)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "110088-K.NARKHEDE COLLEGE OF SCIENCE,BHUSAWAL (Id: C-8850)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "110102-KYDSCT'S COLLEGE OF PHARMACY, SAKEGAON-BHUSAWAL (Id: C-8936)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "110109-LATE DCBEDT'S BIYANI COLLEGE OF EDUCATION, BHUSAWAL (Id: C-8920)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "120017-KES'S PRATAP COLLEGE, AMALNER. (Id: C-8807)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "120018-NPS'S COLLEGE OF EDUCATION, AMALNER. (Id: C-8989)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "120064-SSES'S PANDIT JAWAHARLAL NEHRU B.S.W. & M.S.W. COLLEGE, AMALNER (Id: C-8951)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "120068-DMESS'S ARTS & SCIENCE COLLEGE,AMALNER (Id: C-8985)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "120072-GVSM'S LATE NHANABHAU M.T.PATIL ART COLLEGE,MARWAD,TAL-AMALNER,DIST-JALGAON. (Id: C-8917)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "120104-JBSAS KAMAL AAKKA PATIL ARTS,SCIENCE & COMMERCE COLLGE, AMALNER (Id: C-8879)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "130020-CES'S BP.ARTS,SMA.SCIENCE & KKC.COMMERCE COLLEGE, CHALISGAON. (Id: C-8848)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "130021-RSSPM'S NANASAHEB YASHAVANTRAO N.CHAVAN ARTS,SCIENCE&COMMERCE COLLEGE,CHALISGAON (Id: C-9007)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "130082-SSMACT'S SMT. SITABAI MANGILAL AGRAWAL INSTITUTE OF MANAGEMENT, CHALISGAON (Id: C-8819)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "130083-MPS&SVM'S ARTS COLLEGE, CHALISGAON (Id: C-8961)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "130091-MFS&SVMS MAHATMA PHULE COLLEGE OF EDUCATION, CHALISGAON. (Id: C-8832)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "130106-KDMG'S NANASAHEB DR.UTTAMRAO MAHAJAN COLLEGE OF EDUCATION,KARGAON,TAL-CHALISGAON (Id: C-8814)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "140022-MGTSM'S ARTS,SCIENCE & COMMERCE COLLEGE, CHOPDA. (Id: C-8975)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "140024-CES'S COLLEGE OF EDUCATION, CHOPDA. (Id: C-8982)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "140046-MGSM'S SMT.SHARADCHANDRIKA SURESH PATIL COLLEGE OF PHARMACY, CHOPDA (Id: C-9004)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "140052-BM'S COLLEGE OF SOCIAL STUDIES & SOCIAL WORK, CHOPDA. (Id: C-8823)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "140065-PS&SSS PANKAJ ARTS COLLEGE, CHOPDA (Id: C-8878)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "140068-BMC'S INSTITUTE OF MANAGEMENT & RESEARCH, CHOPDA (Id: C-8909)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "150026-JDMVP CO-OP S'S ARTS,COMMERCE & SCIENCE COLLEGE, YAWAL. (Id: C-8927)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "150027-TMES'S J.T.MAHAJAN COLLEGE OF ENGINEERING, FAIZPUR. (Id: C-9012)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "150028-TVES'S DHANAJI NANA ARTS,SCIENCE & COMMERCE COLLEGE, FAIZPUR. (Id: C-8881)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "150029-TVES'S COLLEGE OF EDUCATION, FAIZPUR. (Id: C-8806)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "150051-TVES'S HON'BLE LOKSEVAK MADHUKARRAO CHAUDHARI COLLEGE OF PHARMACY, FAIZPUR. (Id: C-8851)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "150056-SES'S ARTS & SCIENCE COLLEGE, BHALOD, TAL. YAWAL (Id: C-8820)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "160030-YCSPM'S DADASAHEB D.S.PATIL ARTS,SCIENCE & COMMERCE COLLEGE, ERANDOL. (Id: C-8981)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "160031-PRHSS'S ARTS & COMMERCE COLLEGE, DHARANGAON. (Id: C-8885)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "170032-JTES'S ARTS,COMMERCE & SCIENCE COLLEGE, JAMNER. (Id: C-8983)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "170033-SSE CO-OP S'S LATE R.B.GARUD KALA & WANIJYA MAHAVIDYALAYA, SHENDURNI. (Id: C-8894)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "170034-PT CO-OP ES'S ARTS,SCIENCE & COMMERCE COLLEGE, PACHORA. (Id: C-8980)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "170071-GRAM VIKAS MADAL'S COLLEGE OF ART, PIMPALGAON(HARE),TAL-PACHORA,DIST-JALGAON. (Id: C-8963)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "170079-JJMVPSS'S ARTS COLLEGE, SAMNER, TAL-PACHORA (Id: C-8872)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "170096-SHREE SURESHDADA JAIN INSTITUTE OF PHARMACEUTICAL EDUCATION & RESEARCH, JAMNER (Id: C-8987)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "170111-PDUSPM'S INSTITUTE OF MANAGEMENT & RESEARCH, JAMNER (Id: C-8942)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "180035-VBES'S SANT MUKTABAI ARTS & COMMERCE COLLEGE, MUKTAINAGAR. (Id: C-8880)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "180036-ETES'S S.G.G.K. SCIENCE & S.K.M.C. ARTS & COMMERCE COLLEGE, MUKTAINAGAR. (Id: C-8910)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "180037-RPSPM'S SHRI VITTHALRAO SHANKARRAO NAIK ARTS,COMMERCE & SCIENCE COLLEGE, RAVER. (Id: C-8856)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "180038-JSM'S SGVPC COLLEGE OF EDUCATION, KHIRODA. (Id: C-8891)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "180039-JSM'S SAPTAPUT LALIT KALA MAHAVIDYALAYA, KHIRODA. (Id: C-8935)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "180049-APSPM'S ARTS & SCIENCE COLLEGE, AINPUR. (Id: C-8956)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "180093-MSPM'S SHRI. R.G.MAHAJAN ARTS COLLEGE, TANDALWADI. (Id: C-8966)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "190040-KVPS'S KISAN ARTS,COMMERCE & SCIENCE COLLEGE, PAROLA. (Id: C-8863)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "190041-PTSS'S SAU. RAJNITAI N.DESHMUKH ARTS,COMMERCE & SCIENCE COLLEGE, BHADGAON. (Id: C-8897)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "190042-SSPM'S RANI LAXMIBAI ARTS & SCIENCE COLLEGE, PAROLA. (Id: C-9003)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "190097-SSPM'S COLLEGE OF EDUCATION, TEHU, TAL.PAROLA (Id: C-8901)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "JIJAMATA SHIKSHAN SANSTHAS COLLEGE OF PHARMACY, NANADURBAR (Id: C-47521)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "KAI YASHODABAI DAGADU SARAF CHERITABLE TRUST INSTITUTE OF MANAGEMENT AND SCIENCE, SAKEGAON (Id: C-47522)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "North Maharashtra University, Jalgaon (Id: U-0320)"
        },
        {
            "college_name": "Sri Sant Gadgebaba Hindi College, Bhusaval (Id: C-18221)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Rashtrasant Tukadoji Maharaj Nagpur University, Nagpur (Id: U-0332)"
        },
        {
            "college_name": "Arunodaya Dnyan Prasarak Mandal's (Id: C-44353)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
        },
        {
            "college_name": "Arunodaya Shikshan Prasarak Mandal's (Id: C-44189)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
        },
        {
            "college_name": "Godavari Foundation's Dr. Varsha Patil Women's College of Home Science (Id: C-44240)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
        },
        {
            "college_name": "Laxmi Nirmal Pratishtan Sanchalit's (Id: C-44238)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
        },
        {
            "college_name": "Navalbhau Pratishthan's Rukmanitai Arts & Commerce Mahila College (Id: C-44188)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
        },
        {
            "college_name": "Shivaji Shikshan Prasarak Mandal's Women's College of Education (Id: C-44292)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
        },
        {
            "college_name": "Shri Swami Samarth Mahila Kala Mahavidyalaya (Id: C-44239)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
        },
        {
            "college_name": "Shri Swami Smarth Women's College of Education (Id: C-44128)",
            "college_type": "Affiliated College",
            "district": "Jalgaon",
            "state": "Maharashtra",
            "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
        }
    ]
]
```

 ---------------------------------------

### Getting colleges in a College Type(Affiliated College,Constituent / University College,Recognized Center,PG Center/Off-Campus)

**POST:** */get/collegetype/*



#### Example

**REQUEST :**
```
HOST: localhost:5000
College Type: Consituent
Offset: 0
```

**RESPONSE :**

```json
[
    {
        "college_name": "University COllege of Arts, Commerce and Law (Id: C-32637)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Acharya Nagarjuna University, Guntur (Id: U-0003)"
    },
    {
        "college_name": "University College of Engineering & Technology (Id: C-32695)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Acharya Nagarjuna University, Guntur (Id: U-0003)"
    },
    {
        "college_name": "University College of Pharmaceutical Sciences (Id: C-32766)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Acharya Nagarjuna University, Guntur (Id: U-0003)"
    },
    {
        "college_name": "University College of Physical Education and Sports Sciences (Id: C-32653)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Acharya Nagarjuna University, Guntur (Id: U-0003)"
    },
    {
        "college_name": "University Collge of Architecture & Planning (Id: C-32723)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Acharya Nagarjuna University, Guntur (Id: U-0003)"
    },
    {
        "college_name": "University Collge of Sciences (Id: C-32742)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Acharya Nagarjuna University, Guntur (Id: U-0003)"
    },
    {
        "college_name": "Agricultultural College, Bapatla (Id: C-26378)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Acharya NG Ranga Agricultural University, Hyderabad (Id: U-0004)"
    },
    {
        "college_name": "Agricultural College, Aswaraopet (Id: C-26380)",
        "college_type": "Constituent / University College",
        "district": "Khammam",
        "state": "Telangana",
        "university": "Acharya NG Ranga Agricultural University, Hyderabad (Id: U-0004)"
    },
    {
        "college_name": "Agricultural College, Jagtial (Id: C-26376)",
        "college_type": "Constituent / University College",
        "district": "Karimnagar",
        "state": "Telangana",
        "university": "Acharya NG Ranga Agricultural University, Hyderabad (Id: U-0004)"
    },
    {
        "college_name": "Agricultural College, Mahanandi (Id: C-26377)",
        "college_type": "Constituent / University College",
        "district": "Kurnool",
        "state": "Andhra Pradesh",
        "university": "Acharya NG Ranga Agricultural University, Hyderabad (Id: U-0004)"
    },
    {
        "college_name": "Agricultural College, Naira (Id: C-26375)",
        "college_type": "Constituent / University College",
        "district": "Srikakulam",
        "state": "Andhra Pradesh",
        "university": "Acharya NG Ranga Agricultural University, Hyderabad (Id: U-0004)"
    },
    {
        "college_name": "Agricultural College, Rajahmundry (Id: C-26369)",
        "college_type": "Constituent / University College",
        "district": "East Godavari",
        "state": "Andhra Pradesh",
        "university": "Acharya NG Ranga Agricultural University, Hyderabad (Id: U-0004)"
    },
    {
        "college_name": "Collage of Agriculture, Rajendranagar (Id: C-26372)",
        "college_type": "Constituent / University College",
        "district": "Rangareddy",
        "state": "Telangana",
        "university": "Acharya NG Ranga Agricultural University, Hyderabad (Id: U-0004)"
    },
    {
        "college_name": "College of Agricultural Engineering, Bapatla (Id: C-26373)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Acharya NG Ranga Agricultural University, Hyderabad (Id: U-0004)"
    },
    {
        "college_name": "College of Agricultural Engineering, Madakasira (Id: C-26381)",
        "college_type": "Constituent / University College",
        "district": "Anantapur",
        "state": "Andhra Pradesh",
        "university": "Acharya NG Ranga Agricultural University, Hyderabad (Id: U-0004)"
    },
    {
        "college_name": "College of Food Science and Technology, Bapatla (Id: C-26371)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Acharya NG Ranga Agricultural University, Hyderabad (Id: U-0004)"
    },
    {
        "college_name": "College of Food Science and Technology, Pulivendula (Id: C-26379)",
        "college_type": "Constituent / University College",
        "district": "Y.S.R.",
        "state": "Andhra Pradesh",
        "university": "Acharya NG Ranga Agricultural University, Hyderabad (Id: U-0004)"
    },
    {
        "college_name": "College of Home Science, Hyderabad (Id: C-26370)",
        "college_type": "Constituent / University College",
        "district": "Hyderabad",
        "state": "Telangana",
        "university": "Acharya NG Ranga Agricultural University, Hyderabad (Id: U-0004)"
    },
    {
        "college_name": "S.V. Agricultural College, Tirupathi (Id: C-26374)",
        "college_type": "Constituent / University College",
        "district": "Chittoor",
        "state": "Andhra Pradesh",
        "university": "Acharya NG Ranga Agricultural University, Hyderabad (Id: U-0004)"
    },
    {
        "college_name": "Adesh Institute of Dental Sciences & Research, Baranala Road, Bathinda (Id: C-29246)",
        "college_type": "Constituent / University College",
        "district": "Bathinda",
        "state": "Punjab",
        "university": "ADESH UNIVERSITY (Id: U-0736)"
    },
    {
        "college_name": "Adesh Institute of Medical Sciences & Research, Barnala Road (Id: C-29187)",
        "college_type": "Constituent / University College",
        "district": "Bathinda",
        "state": "Punjab",
        "university": "ADESH UNIVERSITY (Id: U-0736)"
    },
    {
        "college_name": "Adesh Institute of Pharmacy & Biomedical Sciences, Bathinda (Id: C-10496)",
        "college_type": "Constituent / University College",
        "district": "Bathinda",
        "state": "Punjab",
        "university": "ADESH UNIVERSITY (Id: U-0736)"
    },
    {
        "college_name": "College of Nursing, Adesh Institute of Medical Sciences & Research, Bathinda (Id: C-29249)",
        "college_type": "Constituent / University College",
        "district": "Bathinda",
        "state": "Punjab",
        "university": "ADESH UNIVERSITY (Id: U-0736)"
    },
    {
        "college_name": "College of Physiotherapy, Adesh Institute of Medical Sciences & Research, Bathinda (Id: C-29162)",
        "college_type": "Constituent / University College",
        "district": "Bathinda",
        "state": "Punjab",
        "university": "ADESH UNIVERSITY (Id: U-0736)"
    },
    {
        "college_name": "University College of Arts, Commerce and Science (Id: C-7238)",
        "college_type": "Constituent / University College",
        "district": "East Godavari",
        "state": "Andhra Pradesh",
        "university": "Adikavi Nannaya University, Rajahmundry, East Godawari (Id: U-0005)"
    },
    {
        "college_name": "AES INSTITUTE OF COMPUTER STUDIES (Id: C-18)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Ahmedabad University (Id: U-0122)"
    },
    {
        "college_name": "B.K. MAJUMDAR INSTITUTE OF BUSINESS ADMINISTRATION (Id: C-19)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Ahmedabad University (Id: U-0122)"
    },
    {
        "college_name": "H. L. INSTITUTE OF COMMERCE (Id: C-17)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Ahmedabad University (Id: U-0122)"
    },
    {
        "college_name": "H.L. INSTITUTE OF COMPUTER APPLICATIONS (Id: C-16)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Ahmedabad University (Id: U-0122)"
    },
    {
        "college_name": "INSTITUTE OF INFORMATION AND COMMUNICATION TECHNOLOGY, AHMEDABAD (Id: C-47866)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Ahmedabad University (Id: U-0122)"
    },
    {
        "college_name": "INSTITUTE OF LIFE SCIENCE, AHMEDABAD (Id: C-45931)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Ahmedabad University (Id: U-0122)"
    },
    {
        "college_name": "POST GRADUATE INSTITUTE OF MANAGEMENT - AMRUT MODY SCHOOL OF MANAGEMENT (Id: C-15)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Ahmedabad University (Id: U-0122)"
    },
    {
        "college_name": "ALAGAPPA UNIVERSITY CONSTITUENT COLLEGE (Id: C-47507)",
        "college_type": "Constituent / University College",
        "district": "Ramanathapuram",
        "state": "Tamil Nadu",
        "university": "Alagappa University, Alagappa Nagar, Karaikudi (Id: U-0435)"
    },
    {
        "college_name": "WOMEN' S COLLEGE (Id: C-22860)",
        "college_type": "Constituent / University College",
        "district": "Aligarh",
        "state": "Uttar Pradesh",
        "university": "Aligarh Muslim University, Aligarh (Id: U-0496)"
    },
    {
        "college_name": "Amrita School of Business, Coimbatore (Id: C-7023)",
        "college_type": "Constituent / University College",
        "district": "Coimbatore",
        "state": "Tamil Nadu",
        "university": "Amrita Vishwa Vidyapeetham, Coimbatore (Id: U-0436)"
    },
    {
        "college_name": "Amrita School of Engineering, Coimbatore (Id: C-7021)",
        "college_type": "Constituent / University College",
        "district": "Coimbatore",
        "state": "Tamil Nadu",
        "university": "Amrita Vishwa Vidyapeetham, Coimbatore (Id: U-0436)"
    },
    {
        "college_name": "Department of Communication, Coimbatore (Id: C-7024)",
        "college_type": "Constituent / University College",
        "district": "Coimbatore",
        "state": "Tamil Nadu",
        "university": "Amrita Vishwa Vidyapeetham, Coimbatore (Id: U-0436)"
    },
    {
        "college_name": "Department of Social Work, Coimbatore (Id: C-7033)",
        "college_type": "Constituent / University College",
        "district": "Coimbatore",
        "state": "Tamil Nadu",
        "university": "Amrita Vishwa Vidyapeetham, Coimbatore (Id: U-0436)"
    },
    {
        "college_name": "B.A.College of Agricultural , Anand (Id: C-7226)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Anand Agricultural University, Anand (Id: U-0123)"
    },
    {
        "college_name": "College of Agricultural Engineering & Technology, Godhra (Id: C-7228)",
        "college_type": "Constituent / University College",
        "district": "Panch Mahals",
        "state": "Gujarat",
        "university": "Anand Agricultural University, Anand (Id: U-0123)"
    },
    {
        "college_name": "College of Agricultural Information Technology , Anand (Id: C-7229)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Anand Agricultural University, Anand (Id: U-0123)"
    },
    {
        "college_name": "College of Food Processing & Bio Energy , Anand (Id: C-7233)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Anand Agricultural University, Anand (Id: U-0123)"
    },
    {
        "college_name": "College of Veterinary Science & Animal Husbandry, Anand (Id: C-7232)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Anand Agricultural University, Anand (Id: U-0123)"
    },
    {
        "college_name": "International Agri-Business Management Institute , Anand (Id: C-7231)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Anand Agricultural University, Anand (Id: U-0123)"
    },
    {
        "college_name": "Polytechnic in Agricultural Engineering, Dahod (Id: C-7235)",
        "college_type": "Constituent / University College",
        "district": "Dohad",
        "state": "Gujarat",
        "university": "Anand Agricultural University, Anand (Id: U-0123)"
    },
    {
        "college_name": "Polytechnic in Agriculture, Vaso (Id: C-7227)",
        "college_type": "Constituent / University College",
        "district": "Kheda",
        "state": "Gujarat",
        "university": "Anand Agricultural University, Anand (Id: U-0123)"
    },
    {
        "college_name": "Polytechnic in Food Science and Home Economics , Anand (Id: C-7234)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Anand Agricultural University, Anand (Id: U-0123)"
    },
    {
        "college_name": "Sheth D.M.Polytehnic in Horticulture, Vadodara (Id: C-7237)",
        "college_type": "Constituent / University College",
        "district": "Vadodara",
        "state": "Gujarat",
        "university": "Anand Agricultural University, Anand (Id: U-0123)"
    },
    {
        "college_name": "Sheth M.C.College of Dairy Science, Anand (Id: C-7230)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Anand Agricultural University, Anand (Id: U-0123)"
    },
    {
        "college_name": "Sheth M.C.Polytehnic in Agriculture , Anand (Id: C-7236)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Anand Agricultural University, Anand (Id: U-0123)"
    },
    {
        "college_name": "College of Arts & Commerce (Id: C-24240)",
        "college_type": "Constituent / University College",
        "district": "Visakhapatnam",
        "state": "Andhra Pradesh",
        "university": "Andhra University, Visakhapatnam (Id: U-0006)"
    },
    {
        "college_name": "College of Engineering(A) (Id: C-24004)",
        "college_type": "Constituent / University College",
        "district": "Visakhapatnam",
        "state": "Andhra Pradesh",
        "university": "Andhra University, Visakhapatnam (Id: U-0006)"
    },
    {
        "college_name": "College of Engineering for Women (Id: C-23966)",
        "college_type": "Constituent / University College",
        "district": "Visakhapatnam",
        "state": "Andhra Pradesh",
        "university": "Andhra University, Visakhapatnam (Id: U-0006)"
    },
    {
        "college_name": "College of Pharmaceutical Sciences (Id: C-24055)",
        "college_type": "Constituent / University College",
        "district": "Visakhapatnam",
        "state": "Andhra Pradesh",
        "university": "Andhra University, Visakhapatnam (Id: U-0006)"
    },
    {
        "college_name": "College of Science & Technology (Id: C-24101)",
        "college_type": "Constituent / University College",
        "district": "Visakhapatnam",
        "state": "Andhra Pradesh",
        "university": "Andhra University, Visakhapatnam (Id: U-0006)"
    },
    {
        "college_name": "Dr.B.R.Ambedkar College of Law (Id: C-23907)",
        "college_type": "Constituent / University College",
        "district": "Visakhapatnam",
        "state": "Andhra Pradesh",
        "university": "Andhra University, Visakhapatnam (Id: U-0006)"
    },
    {
        "college_name": "A.C. College of Technology Campus (Id: C-25071)",
        "college_type": "Constituent / University College",
        "district": "Chennai",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "Anna University of Technology Madurai, Dindigul Campus (Id: C-26786)",
        "college_type": "Constituent / University College",
        "district": "Dindigul",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "Anna University of Technology Madurai, Madurai Campus (Id: C-26778)",
        "college_type": "Constituent / University College",
        "district": "Madurai",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "Anna University of Technology Madurai, Ramnad Campus (Id: C-26803)",
        "college_type": "Constituent / University College",
        "district": "Ramanathapuram",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "Anna University of Technology, Tiruchirappalli - Ariyalur Campus (Id: C-25048)",
        "college_type": "Constituent / University College",
        "district": "Ariyalur",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "Anna University of Technology Tiruchirappalli - Panruti Campus (Id: C-25056)",
        "college_type": "Constituent / University College",
        "district": "Cuddalore",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "Anna University of Technology Tiruchirappalli - Pattukkottai Campus (Id: C-24997)",
        "college_type": "Constituent / University College",
        "district": "Thanjavur",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "Anna University of Technology Tiruchirappalli - Tirukkuvalai Campus (Id: C-25034)",
        "college_type": "Constituent / University College",
        "district": "Nagapattinam",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "College of Engg., Guindy Campus (Id: C-25072)",
        "college_type": "Constituent / University College",
        "district": "Chennai",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "Madras Institute of Technology Campus (Id: C-25070)",
        "college_type": "Constituent / University College",
        "district": "Chennai",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "School of Architecture & Planning Campus (Id: C-25073)",
        "college_type": "Constituent / University College",
        "district": "Chennai",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "University College of Engineering Arni (Id: C-16472)",
        "college_type": "Constituent / University College",
        "district": "Tiruvannamalai",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "University College of Engineering Kancheepuram (Id: C-16461)",
        "college_type": "Constituent / University College",
        "district": "Kancheepuram",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "University College of Engineering Nagercoil (Id: C-27035)",
        "college_type": "Constituent / University College",
        "district": "Kanniyakumari",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "University College of Engineering Tindivanam (Id: C-16598)",
        "college_type": "Constituent / University College",
        "district": "Viluppuram",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "University College of Engineering Villupuram (Id: C-16587)",
        "college_type": "Constituent / University College",
        "district": "Viluppuram",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "University Departments of Anna University of Technology Tirunelveli (Id: C-27033)",
        "college_type": "Constituent / University College",
        "district": "Tirunelveli",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "University V.O.Chidambaranar College of Engineering Tuticorin (Id: C-27060)",
        "college_type": "Constituent / University College",
        "district": "Thoothukkudi",
        "state": "Tamil Nadu",
        "university": "Anna University, Chennai (Id: U-0439)"
    },
    {
        "college_name": "Patna Dental College (Id: C-43235)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Aryabhatta Knoweledge University , Patna (Id: U-0057)"
    },
    {
        "college_name": "Patna Medical College (Id: C-43236)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Aryabhatta Knoweledge University , Patna (Id: U-0057)"
    },
    {
        "college_name": "Biswanath College of Agriculture (Id: C-24843)",
        "college_type": "Constituent / University College",
        "district": "Sonitpur",
        "state": "Assam",
        "university": "Assam Agricultural University, Jorhat (Id: U-0048)"
    },
    {
        "college_name": "College of Agriculture (Id: C-24841)",
        "college_type": "Constituent / University College",
        "district": "Jorhat",
        "state": "Assam",
        "university": "Assam Agricultural University, Jorhat (Id: U-0048)"
    },
    {
        "college_name": "College of Fisheries Science (Id: C-24842)",
        "college_type": "Constituent / University College",
        "district": "Nagaon",
        "state": "Assam",
        "university": "Assam Agricultural University, Jorhat (Id: U-0048)"
    },
    {
        "college_name": "College of Home Science (Id: C-24844)",
        "college_type": "Constituent / University College",
        "district": "Jorhat",
        "state": "Assam",
        "university": "Assam Agricultural University, Jorhat (Id: U-0048)"
    },
    {
        "college_name": "College of Veterinary Science (Id: C-24845)",
        "college_type": "Constituent / University College",
        "district": "Kamrup",
        "state": "Assam",
        "university": "Assam Agricultural University, Jorhat (Id: U-0048)"
    },
    {
        "college_name": "Don Bosco Institute of Management (Id: C-1229)",
        "college_type": "Constituent / University College",
        "district": "Kamrup",
        "state": "Assam",
        "university": "Assam Don Bosco University, Guwahati (Id: U-0049)"
    },
    {
        "college_name": "Guru Gobind Singh Medical College, Sadiq Road, Faridkot (Id: C-29238)",
        "college_type": "Constituent / University College",
        "district": "Faridkot",
        "state": "Punjab",
        "university": "Baba Farid University of Health & Medical Sciences, Faridkot (Id: U-0371)"
    },
    {
        "college_name": "State Institute of Nursing & Paramedical Sciences, Badal (Id: C-29167)",
        "college_type": "Constituent / University College",
        "district": "Muktsar",
        "state": "Punjab",
        "university": "Baba Farid University of Health & Medical Sciences, Faridkot (Id: U-0371)"
    },
    {
        "college_name": "University College of Nursing, Faridkot (Id: C-29137)",
        "college_type": "Constituent / University College",
        "district": "Faridkot",
        "state": "Punjab",
        "university": "Baba Farid University of Health & Medical Sciences, Faridkot (Id: U-0371)"
    },
    {
        "college_name": "University College of Physiotherapy, Faridkot (Id: C-29143)",
        "college_type": "Constituent / University College",
        "district": "Faridkot",
        "state": "Punjab",
        "university": "Baba Farid University of Health & Medical Sciences, Faridkot (Id: U-0371)"
    },
    {
        "college_name": "Braj Mohan Das College, Dayalpur, Vaishali (Id: C-19035)",
        "college_type": "Constituent / University College",
        "district": "Vaishali",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "C.N.D. Sahebganj, Muzaffarpur (Id: C-19011)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Deochand College, Hajipur (Id: C-19010)",
        "college_type": "Constituent / University College",
        "district": "Vaishali",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Dr. Krishna Singh mahila College, Motihari (Id: C-19023)",
        "college_type": "Constituent / University College",
        "district": "Purba Champaran",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Dr. Ram Manohar Lohiya Smarak College, Muzaffarpur (Id: C-18985)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Hawaharlal Nehru Memorial College, Ghorasahan (Id: C-18995)",
        "college_type": "Constituent / University College",
        "district": "Purba Champaran",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Jang Bahadur Singh Dhanaur College, Bakuchi, Muzaffarpur (Id: C-19017)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Jiwachh College, Motipur, Muzaffarpur (Id: C-18997)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "J.L.College, Hajipur (Id: C-19012)",
        "college_type": "Constituent / University College",
        "district": "Vaishali",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "J.S.College, Chandaul, Sitamarhi (Id: C-18993)",
        "college_type": "Constituent / University College",
        "district": "Sitamarhi",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Khemchand Tarachand College, Raxaul (Id: C-19021)",
        "college_type": "Constituent / University College",
        "district": "Purba Champaran",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Laxmi Narayan College, Bhagwanpur, Vaishali (Id: C-18981)",
        "college_type": "Constituent / University College",
        "district": "Vaishali",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "L.N.D. College, Motihari (Id: C-19018)",
        "college_type": "Constituent / University College",
        "district": "Sitamarhi",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "L.N.T. College, Muzaffarpur (Id: C-19009)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "L.S.College, Muzaffarpur (Id: C-19014)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Mahant Shi'vshankar Giri College, Areraj, East Champaran (Id: C-19000)",
        "college_type": "Constituent / University College",
        "district": "Purba Champaran",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "M.D.D.M. College, Muzaffarpur (Id: C-18996)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "M.J.K. College, Bettiah (Id: C-19030)",
        "college_type": "Constituent / University College",
        "district": "Pashchim Champaran",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "M.P.S. Sc. College, Muzaffarpur (Id: C-19031)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "MSKB College, Muzaffarpur (Id: C-18998)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Munshi Singh College, Motihari (Id: C-19001)",
        "college_type": "Constituent / University College",
        "district": "Purba Champaran",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Nitishwar College, Muzaffarpur (Id: C-19022)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Rameshwar Singh College, Muzaffarpur (Id: C-19033)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Ramsewak Singh Mahila College, Sitamarhi (Id: C-18989)",
        "college_type": "Constituent / University College",
        "district": "Sitamarhi",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "R.B.B.M. College, Muzaffarpur (Id: C-19016)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "R.C.College, Dholi, Sakra, Muzaffarpur (Id: C-18980)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "R.D.S.College, Muzaffarpur (Id: C-19020)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "R.L.S.Y. College, Bettiah (Id: C-19019)",
        "college_type": "Constituent / University College",
        "district": "Pashchim Champaran",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "R.N. College, Hajipur (Id: C-19029)",
        "college_type": "Constituent / University College",
        "district": "Vaishali",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "R.P.S. College, Chakiya, East Champaran (Id: C-18990)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "R.S.S.Sc. College, Sitamarhi (Id: C-18983)",
        "college_type": "Constituent / University College",
        "district": "Sitamarhi",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Samta College, Jandaha, Vaishali (Id: C-18991)",
        "college_type": "Constituent / University College",
        "district": "Vaishali",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Shiv Deni Ram Ayodhya Prasad College, Barachakia (Id: C-19024)",
        "college_type": "Constituent / University College",
        "district": "Purba Champaran",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Shri Ramkrishna Goyanka College, Sitamarhi (Id: C-18986)",
        "college_type": "Constituent / University College",
        "district": "Sitamarhi",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Sri Laxmi Kishori College, Sitamarhi (Id: C-19032)",
        "college_type": "Constituent / University College",
        "district": "Sitamarhi",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Sri Narayan Singh College, Motihari (Id: C-19007)",
        "college_type": "Constituent / University College",
        "district": "Purba Champaran",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Sri Raghav Prasad Singh College, Jaintpur, Muzaffarpur (Id: C-19006)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Tarkeshwar Prsasad Verma College, Narkatiyaganj (Id: C-19013)",
        "college_type": "Constituent / University College",
        "district": "Pashchim Champaran",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Vaishali Mahila College, Hajipur (Id: C-19008)",
        "college_type": "Constituent / University College",
        "district": "Vaishali",
        "state": "Bihar",
        "university": "Babasaheb Bhimrao Ambedkar Bihar University, Muzaffarpur (Id: U-0058)"
    },
    {
        "college_name": "Institute of Emerging Sciences & Technology (Id: C-22474)",
        "college_type": "Constituent / University College",
        "district": "Solan",
        "state": "Himachal Pradesh",
        "university": "Baddi University of Emerging Sciences and Technology, Budha (Makhnumajra), Solan (Id: U-0177)"
    },
    {
        "college_name": "Institute of Management Studies (Id: C-22473)",
        "college_type": "Constituent / University College",
        "district": "Solan",
        "state": "Himachal Pradesh",
        "university": "Baddi University of Emerging Sciences and Technology, Budha (Makhnumajra), Solan (Id: U-0177)"
    },
    {
        "college_name": "Institute of Pharmacy & Emerging Sciences (Id: C-22475)",
        "college_type": "Constituent / University College",
        "district": "Solan",
        "state": "Himachal Pradesh",
        "university": "Baddi University of Emerging Sciences and Technology, Budha (Makhnumajra), Solan (Id: U-0177)"
    },
    {
        "college_name": "Mahila Maha Vidyalaya (Id: C-21250)",
        "college_type": "Constituent / University College",
        "district": "Varanasi",
        "state": "Uttar Pradesh",
        "university": "Banaras Hindu University, Banaras (Id: U-0500)"
    },
    {
        "college_name": "University College of Physical Education (Id: C-17611)",
        "college_type": "Constituent / University College",
        "district": "Bangalore",
        "state": "Karnataka",
        "university": "Bangalore University, Bangalore (Id: U-0215)"
    },
    {
        "college_name": "University Law College (Id: C-17610)",
        "college_type": "Constituent / University College",
        "district": "Bangalore",
        "state": "Karnataka",
        "university": "Bangalore University, Bangalore (Id: U-0215)"
    },
    {
        "college_name": "University Vishweshwaraya College of Engineering (Id: C-17613)",
        "college_type": "Constituent / University College",
        "district": "Bangalore",
        "state": "Karnataka",
        "university": "Bangalore University, Bangalore (Id: U-0215)"
    },
    {
        "college_name": "Lingaraj Law College, Berhampur (Id: C-39443)",
        "college_type": "Constituent / University College",
        "district": "Ganjam",
        "state": "Odisha",
        "university": "Berhampur University, Berhampur (Id: U-0350)"
    },
    {
        "college_name": "BPS College of Education (Id: C-17084)",
        "college_type": "Constituent / University College",
        "district": "Sonipat",
        "state": "Haryana",
        "university": "Bhagat Phool Singh Mahila University, Khanpur Kalan, Sonipat (Id: U-0157)"
    },
    {
        "college_name": "BPSM Girls College (Id: C-17085)",
        "college_type": "Constituent / University College",
        "district": "Sonipat",
        "state": "Haryana",
        "university": "Bhagat Phool Singh Mahila University, Khanpur Kalan, Sonipat (Id: U-0157)"
    },
    {
        "college_name": "MSM Institute of Ayurveda (Id: C-41025)",
        "college_type": "Constituent / University College",
        "district": "Sonipat",
        "state": "Haryana",
        "university": "Bhagat Phool Singh Mahila University, Khanpur Kalan, Sonipat (Id: U-0157)"
    },
    {
        "college_name": "School of Pharmaceutical Education and Research (Id: C-17087)",
        "college_type": "Constituent / University College",
        "district": "Sonipat",
        "state": "Haryana",
        "university": "Bhagat Phool Singh Mahila University, Khanpur Kalan, Sonipat (Id: U-0157)"
    },
    {
        "college_name": "Bharathiar University Arts and science College (Id: C-41114)",
        "college_type": "Constituent / University College",
        "district": "Coimbatore",
        "state": "Tamil Nadu",
        "university": "Bharathiar University, Coimbatore (Id: U-0447)"
    },
    {
        "college_name": "Bharathiar University Arts and Science College (Id: C-41041)",
        "college_type": "Constituent / University College",
        "district": "Erode",
        "state": "Tamil Nadu",
        "university": "Bharathiar University, Coimbatore (Id: U-0447)"
    },
    {
        "college_name": "Bharathiar University College of Arts and Science (Id: C-41117)",
        "college_type": "Constituent / University College",
        "district": "The Nilgiris",
        "state": "Tamil Nadu",
        "university": "Bharathiar University, Coimbatore (Id: U-0447)"
    },
    {
        "college_name": "Bharathidasan University College, Orathanadu - 614 625 (Id: C-35816)",
        "college_type": "Constituent / University College",
        "district": "Thanjavur",
        "state": "Tamil Nadu",
        "university": "Bharathidasan University, Tiruchirappalli (Id: U-0448)"
    },
    {
        "college_name": "Bharathidasan University Constituent Arts & Science College (Co-education), Inamkulathur, Tiruchirappalli (Id: C-35898)",
        "college_type": "Constituent / University College",
        "district": "Tiruchirappalli",
        "state": "Tamil Nadu",
        "university": "Bharathidasan University, Tiruchirappalli (Id: U-0448)"
    },
    {
        "college_name": "Bharathidasan University Constituent Arts & Science College (Co-education), Kaadambadi (Id: C-35785)",
        "college_type": "Constituent / University College",
        "district": "Nagapattinam",
        "state": "Tamil Nadu",
        "university": "Bharathidasan University, Tiruchirappalli (Id: U-0448)"
    },
    {
        "college_name": "Bharathidasan University Constituent College, Lalgudi - 621 601 (Id: C-35806)",
        "college_type": "Constituent / University College",
        "district": "Tiruchirappalli",
        "state": "Tamil Nadu",
        "university": "Bharathidasan University, Tiruchirappalli (Id: U-0448)"
    },
    {
        "college_name": "Bharathidasan University, Kurumbalur - 621 107 (Id: C-35876)",
        "college_type": "Constituent / University College",
        "district": "Perambalur",
        "state": "Tamil Nadu",
        "university": "Bharathidasan University, Tiruchirappalli (Id: U-0448)"
    },
    {
        "college_name": "Bharathidasan University Model College, Aranthangi - 614 616 (Id: C-35855)",
        "college_type": "Constituent / University College",
        "district": "Pudukkottai",
        "state": "Tamil Nadu",
        "university": "Bharathidasan University, Tiruchirappalli (Id: U-0448)"
    },
    {
        "college_name": "Bharathidasan University Model College, Thiruthuraipoondi - 614 713 (Id: C-35817)",
        "college_type": "Constituent / University College",
        "district": "Thiruvarur",
        "state": "Tamil Nadu",
        "university": "Bharathidasan University, Tiruchirappalli (Id: U-0448)"
    },
    {
        "college_name": "Bharathidasan University Model College, Vedaranyam - 614 810 (Id: C-35779)",
        "college_type": "Constituent / University College",
        "district": "Nagapattinam",
        "state": "Tamil Nadu",
        "university": "Bharathidasan University, Tiruchirappalli (Id: U-0448)"
    },
    {
        "college_name": "Abhijit Kadam Insttute of Management and social sciences,solapur (Id: C-35436)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "College of Architecture, Pune (Id: C-35439)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "College of Ayurved, Pune (Id: C-35433)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "College of Engineering, Pune (Id: C-35417)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "College of Nurisng, Navi Mumbai (Id: C-35431)",
        "college_type": "Constituent / University College",
        "district": "Thane",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "College of Nursing, Pune (Id: C-35426)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "College of Nursing, Sangli (Id: C-35437)",
        "college_type": "Constituent / University College",
        "district": "Sangli",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "College of Physical Education, Pune (Id: C-35438)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Dental College and Hospital, Navi Mumbai (Id: C-35419)",
        "college_type": "Constituent / University College",
        "district": "Thane",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Dental College and Hospital, Pune (Id: C-35422)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Dental College and Hospital, Sangli (Id: C-35415)",
        "college_type": "Constituent / University College",
        "district": "Sangli",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Homeopathic Medical College, Pune (Id: C-35418)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Institute of Environment Education and Research, Pune (Id: C-35425)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Institute of Hotel Management and Catering Technology, Pune (Id: C-35434)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Institute of Management and Entrepreneurship Development, Pune (Id: C-35429)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Institute of Management and Research, New Delhi (Id: C-35440)",
        "college_type": "Constituent / University College",
        "district": "New Delhi",
        "state": "Delhi",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Institute of Management and Rural Development Administration, Sangli (Id: C-35432)",
        "college_type": "Constituent / University College",
        "district": "Sangli",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Institute of Management, Kolhapur (Id: C-35421)",
        "college_type": "Constituent / University College",
        "district": "Kolhapur",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Interactive Research School for Health Affairs, Pune (Id: C-35442)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Medical College and Hospital, Sangli (Id: C-35443)",
        "college_type": "Constituent / University College",
        "district": "Sangli",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Medical College, Pune (Id: C-35423)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "New Law College, Pune (Id: C-35428)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Poona College of Pharmacy, Pune (Id: C-35430)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Rajiv Gandhi Institute of Information Technology and Biotechnology, Pune (Id: C-35416)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Research and Development for Pharmaceutical Sciences and Applied Chemistry, Pune (Id: C-35420)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Social Science Centre, Pune (Id: C-35441)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Yashwantrao Chavan Institute of Social Science Studies and Research, Pune (Id: C-35427)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Yashwantrao Mohite College of Arts, Science and Commerce, Pune (Id: C-35424)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Yashwantrao Mohite Institute of Management, Karad (Id: C-35435)",
        "college_type": "Constituent / University College",
        "district": "Satara",
        "state": "Maharashtra",
        "university": "Bharati Vidyapeeth, Pune (Id: U-0292)"
    },
    {
        "college_name": "Araria College, Araria (Id: C-29616)",
        "college_type": "Constituent / University College",
        "district": "Araria",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "B.N.M.V. College, Sahugadh (Id: C-29577)",
        "college_type": "Constituent / University College",
        "district": "Madhepura",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "B.S.S. College, Supaul (Id: C-29615)",
        "college_type": "Constituent / University College",
        "district": "Supaul",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "D.S. College, Katihar (Id: C-29628)",
        "college_type": "Constituent / University College",
        "district": "Katihar",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "Forbishganj College, Forbisganj (Id: C-29606)",
        "college_type": "Constituent / University College",
        "district": "Araria",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "G.L.M. College, Banmankhi (Id: C-29627)",
        "college_type": "Constituent / University College",
        "district": "Purnia",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "H.S. College, Udakishunganj (Id: C-29593)",
        "college_type": "Constituent / University College",
        "district": "Madhepura",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "K.B. Jha College, Katihar (Id: C-29600)",
        "college_type": "Constituent / University College",
        "district": "Katihar",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "K.P. College, Murliganj (Id: C-29580)",
        "college_type": "Constituent / University College",
        "district": "Madhepura",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "L.N.M.S. College, Birpur (Id: C-29602)",
        "college_type": "Constituent / University College",
        "district": "Supaul",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "Marwari College, Kishanganj (Id: C-29605)",
        "college_type": "Constituent / University College",
        "district": "Kishanganj",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "M.H.M. College, Sonbarsa (Id: C-29639)",
        "college_type": "Constituent / University College",
        "district": "Saharsa",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "M.J.M. Mahila College, Katihar (Id: C-29631)",
        "college_type": "Constituent / University College",
        "district": "Katihar",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "M.L. Arya College, Kasba (Id: C-29612)",
        "college_type": "Constituent / University College",
        "district": "Purnia",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "M.L.T. College, Saharsa (Id: C-29614)",
        "college_type": "Constituent / University College",
        "district": "Saharsa",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "Nehru College, Bahadurganj (Id: C-29601)",
        "college_type": "Constituent / University College",
        "district": "Kishanganj",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "Nirmali College, Nirmali (Id: C-29624)",
        "college_type": "Constituent / University College",
        "district": "Supaul",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "P.Sc. College, Madhepura (Id: C-29589)",
        "college_type": "Constituent / University College",
        "district": "Madhepura",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "Purnia College, Purnia (Id: C-29625)",
        "college_type": "Constituent / University College",
        "district": "Purnia",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "Purnia Mahila College, Purnia (Id: C-29584)",
        "college_type": "Constituent / University College",
        "district": "Purnia",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "R.D.S. College, Salmari (Id: C-29640)",
        "college_type": "Constituent / University College",
        "district": "Katihar",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "R.Jha Mahila College, Saharsa (Id: C-29608)",
        "college_type": "Constituent / University College",
        "district": "Saharsa",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "R.L. College, Madhawnagar (Id: C-29609)",
        "college_type": "Constituent / University College",
        "district": "Purnia",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "R.M. College, Saharsa (Id: C-29632)",
        "college_type": "Constituent / University College",
        "district": "Saharsa",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "R.M.M. Law College, Saharsa (Id: C-29603)",
        "college_type": "Constituent / University College",
        "district": "Saharsa",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "S.N.S.R.K.S. College, Saharsa (Id: C-29579)",
        "college_type": "Constituent / University College",
        "district": "Saharsa",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "T.P. College, Madhepura (Id: C-29582)",
        "college_type": "Constituent / University College",
        "district": "Madhepura",
        "state": "Bihar",
        "university": "Bhupendra Narayan Mandal University, Madhepura (Id: U-0059)"
    },
    {
        "college_name": "Bhola Prasad Shastri Agricultural College, Purnia (Id: C-8349)",
        "college_type": "Constituent / University College",
        "district": "Purnia",
        "state": "Bihar",
        "university": "Bihar Agriculture University, Sabour (Id: U-0060)"
    },
    {
        "college_name": "Bihar Agricultural College, Sabour (Id: C-8347)",
        "college_type": "Constituent / University College",
        "district": "Bhagalpur",
        "state": "Bihar",
        "university": "Bihar Agriculture University, Sabour (Id: U-0060)"
    },
    {
        "college_name": "Bihar Veterinary College, Patna (Id: C-8350)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Bihar Agriculture University, Sabour (Id: U-0060)"
    },
    {
        "college_name": "College of Horticulture, Noorsarai (Id: C-8346)",
        "college_type": "Constituent / University College",
        "district": "Nalanda",
        "state": "Bihar",
        "university": "Bihar Agriculture University, Sabour (Id: U-0060)"
    },
    {
        "college_name": "Mandan Bharti Agricultural College, Agwanpur (Id: C-8348)",
        "college_type": "Constituent / University College",
        "district": "Saharsa",
        "state": "Bihar",
        "university": "Bihar Agriculture University, Sabour (Id: U-0060)"
    },
    {
        "college_name": "Sanjay Gandhi Institute of Dairy Technology, Patna (Id: C-8351)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Bihar Agriculture University, Sabour (Id: U-0060)"
    },
    {
        "college_name": "Veer Kunwar Singh College of Agriculture, Dumraon (Id: C-8352)",
        "college_type": "Constituent / University College",
        "district": "Buxar",
        "state": "Bihar",
        "university": "Bihar Agriculture University, Sabour (Id: U-0060)"
    },
    {
        "college_name": "Centre for IT Education, Bhubaneswar (Id: C-30082)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Biju Patnaik University of Technology, Rourkela (Id: U-0351)"
    },
    {
        "college_name": "College of Engineering & Technology, Bhubaneswar (Id: C-30047)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Biju Patnaik University of Technology, Rourkela (Id: U-0351)"
    },
    {
        "college_name": "Government College of Engineering, Kalahandi (Id: C-30046)",
        "college_type": "Constituent / University College",
        "district": "Kalahandi",
        "state": "Odisha",
        "university": "Biju Patnaik University of Technology, Rourkela (Id: U-0351)"
    },
    {
        "college_name": "Government College of Engineering, Keonjhar (Id: C-30049)",
        "college_type": "Constituent / University College",
        "district": "Kendujhar",
        "state": "Odisha",
        "university": "Biju Patnaik University of Technology, Rourkela (Id: U-0351)"
    },
    {
        "college_name": "Institute of Management & Information Technology, Cuttack (Id: C-30099)",
        "college_type": "Constituent / University College",
        "district": "Cuttack",
        "state": "Odisha",
        "university": "Biju Patnaik University of Technology, Rourkela (Id: U-0351)"
    },
    {
        "college_name": "Parala Maharaja Engineering College, Berhampur (Id: C-30068)",
        "college_type": "Constituent / University College",
        "district": "Ganjam",
        "state": "Odisha",
        "university": "Biju Patnaik University of Technology, Rourkela (Id: U-0351)"
    },
    {
        "college_name": "Shri B. M. Patil Medical College & Research Centre (Id: C-8334)",
        "college_type": "Constituent / University College",
        "district": "Bijapur",
        "state": "Karnataka",
        "university": "B.L.D.E. University, Bijapur (Id: U-0214)"
    },
    {
        "college_name": "M.L.B. College (Id: C-22603)",
        "college_type": "Constituent / University College",
        "district": "Jhansi",
        "state": "Uttar Pradesh",
        "university": "Bundelkhand University, Jhansi (Id: U-0502)"
    },
    {
        "college_name": "Bankura Christian College (Id: C-44742)",
        "college_type": "Constituent / University College",
        "district": "Bankura",
        "state": "West Bengal",
        "university": "Burdwan University, Burdwan (Id: U-0569)"
    },
    {
        "college_name": "Banwarilal Bhalotia College (Id: C-44735)",
        "college_type": "Constituent / University College",
        "district": "Barddhaman",
        "state": "West Bengal",
        "university": "Burdwan University, Burdwan (Id: U-0569)"
    },
    {
        "college_name": "Burdwan Raj College (Id: C-44787)",
        "college_type": "Constituent / University College",
        "district": "Barddhaman",
        "state": "West Bengal",
        "university": "Burdwan University, Burdwan (Id: U-0569)"
    },
    {
        "college_name": "Chandernagore Government College (Id: C-44744)",
        "college_type": "Constituent / University College",
        "district": "Hugli",
        "state": "West Bengal",
        "university": "Burdwan University, Burdwan (Id: U-0569)"
    },
    {
        "college_name": "Durgapur Government College (Id: C-44764)",
        "college_type": "Constituent / University College",
        "district": "Barddhaman",
        "state": "West Bengal",
        "university": "Burdwan University, Burdwan (Id: U-0569)"
    },
    {
        "college_name": "Hooghly Mohsin College (Id: C-44699)",
        "college_type": "Constituent / University College",
        "district": "Hugli",
        "state": "West Bengal",
        "university": "Burdwan University, Burdwan (Id: U-0569)"
    },
    {
        "college_name": "M.U.C. Women's College (Id: C-44657)",
        "college_type": "Constituent / University College",
        "district": "Barddhaman",
        "state": "West Bengal",
        "university": "Burdwan University, Burdwan (Id: U-0569)"
    },
    {
        "college_name": "Netaji Mahavidyalaya (Id: C-44652)",
        "college_type": "Constituent / University College",
        "district": "Hugli",
        "state": "West Bengal",
        "university": "Burdwan University, Burdwan (Id: U-0569)"
    },
    {
        "college_name": "Pandit Raghunath Murmu Smriti Mahavidyalaya (Id: C-44670)",
        "college_type": "Constituent / University College",
        "district": "Bankura",
        "state": "West Bengal",
        "university": "Burdwan University, Burdwan (Id: U-0569)"
    },
    {
        "college_name": "Ramananda College (Id: C-44757)",
        "college_type": "Constituent / University College",
        "district": "Bankura",
        "state": "West Bengal",
        "university": "Burdwan University, Burdwan (Id: U-0569)"
    },
    {
        "college_name": "Suri Vidyasagar College (Id: C-44791)",
        "college_type": "Constituent / University College",
        "district": "Birbhum",
        "state": "West Bengal",
        "university": "Burdwan University, Burdwan (Id: U-0569)"
    },
    {
        "college_name": "Vivekananda Mahavidyalaya, Burdwan (Id: C-44732)",
        "college_type": "Constituent / University College",
        "district": "Barddhaman",
        "state": "West Bengal",
        "university": "Burdwan University, Burdwan (Id: U-0569)"
    },
    {
        "college_name": "Calorx Institute of Education (Id: C-16755)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Carlox Teacher's University, Ahmedabad (Id: U-0125)"
    },
    {
        "college_name": "College of Agricultural Engineering and Post Harvest Technology, Ranipool, Gangtok (Id: C-26829)",
        "college_type": "Constituent / University College",
        "district": "East District",
        "state": "Sikkim",
        "university": "Central Agricultural University, Imphal (Id: U-0336)"
    },
    {
        "college_name": "College of Agriculture, Imphal (Id: C-26831)",
        "college_type": "Constituent / University College",
        "district": "Imphal West",
        "state": "Manipur",
        "university": "Central Agricultural University, Imphal (Id: U-0336)"
    },
    {
        "college_name": "College of Fisheries, Lembucherrra (Id: C-26834)",
        "college_type": "Constituent / University College",
        "district": "West Tripura",
        "state": "Tripura",
        "university": "Central Agricultural University, Imphal (Id: U-0336)"
    },
    {
        "college_name": "College of Home Science, Tura (Id: C-26830)",
        "college_type": "Constituent / University College",
        "district": "West Garo Hills",
        "state": "Meghalaya",
        "university": "Central Agricultural University, Imphal (Id: U-0336)"
    },
    {
        "college_name": "College of Horticulture and Forestry, Pasighat (Id: C-26828)",
        "college_type": "Constituent / University College",
        "district": "East Siang",
        "state": "Arunachal Pradesh",
        "university": "Central Agricultural University, Imphal (Id: U-0336)"
    },
    {
        "college_name": "College of Post Graduate Studies, Umiam (Id: C-26832)",
        "college_type": "Constituent / University College",
        "district": "Ribhoi",
        "state": "Meghalaya",
        "university": "Central Agricultural University, Imphal (Id: U-0336)"
    },
    {
        "college_name": "College of Veterinary sciences & Animal Husbandry, Aizawl (Id: C-26833)",
        "college_type": "Constituent / University College",
        "district": "Aizawl",
        "state": "Mizoram",
        "university": "Central Agricultural University, Imphal (Id: U-0336)"
    },
    {
        "college_name": "School of Engineering & Technology (JITM), Paralakhemundi (Id: C-16458)",
        "college_type": "Constituent / University College",
        "district": "Gajapati",
        "state": "Odisha",
        "university": "Centurion University of Technology and Management (Id: U-0353)"
    },
    {
        "college_name": "College of Agriculture (Id: C-27192)",
        "college_type": "Constituent / University College",
        "district": "Kanpur Nagar",
        "state": "Uttar Pradesh",
        "university": "Chandra Shekhar Azad University of Agriculture & Technology, Kanpur (Id: U-0504)"
    },
    {
        "college_name": "College of Forestry (Id: C-27191)",
        "college_type": "Constituent / University College",
        "district": "Kanpur Nagar",
        "state": "Uttar Pradesh",
        "university": "Chandra Shekhar Azad University of Agriculture & Technology, Kanpur (Id: U-0504)"
    },
    {
        "college_name": "College of Horticulture (Id: C-27194)",
        "college_type": "Constituent / University College",
        "district": "Kanpur Nagar",
        "state": "Uttar Pradesh",
        "university": "Chandra Shekhar Azad University of Agriculture & Technology, Kanpur (Id: U-0504)"
    },
    {
        "college_name": "Dr. B.R. Ambedkar Engineering College (Id: C-27190)",
        "college_type": "Constituent / University College",
        "district": "Etawah",
        "state": "Uttar Pradesh",
        "university": "Chandra Shekhar Azad University of Agriculture & Technology, Kanpur (Id: U-0504)"
    },
    {
        "college_name": "Maharani Avanti Bai College of Homescience (Id: C-27193)",
        "college_type": "Constituent / University College",
        "district": "Kanpur Nagar",
        "state": "Uttar Pradesh",
        "university": "Chandra Shekhar Azad University of Agriculture & Technology, Kanpur (Id: U-0504)"
    },
    {
        "college_name": "Chandubhai S. Patel Institute of Technology (Id: C-16183)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Charotar University of Science & Technology, Anand (Id: U-0128)"
    },
    {
        "college_name": "Charotar Institute of Physiotherapy (Id: C-16182)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Charotar University of Science & Technology, Anand (Id: U-0128)"
    },
    {
        "college_name": "Indukaka Ipcowala Institute of Management (Id: C-16184)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Charotar University of Science & Technology, Anand (Id: U-0128)"
    },
    {
        "college_name": "Manikaka Topawala Institute of Nursing (Id: C-16181)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Charotar University of Science & Technology, Anand (Id: U-0128)"
    },
    {
        "college_name": "P. D. Patel Institute of Applied Sciences (Id: C-16178)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Charotar University of Science & Technology, Anand (Id: U-0128)"
    },
    {
        "college_name": "Ramanbhai Patel College of Pharmacy (Id: C-16179)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Charotar University of Science & Technology, Anand (Id: U-0128)"
    },
    {
        "college_name": "Smt. Chandaben Mohanbhai Patel Institute of Computer Applications (Id: C-16180)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Charotar University of Science & Technology, Anand (Id: U-0128)"
    },
    {
        "college_name": "G.S.V.M. MEDICAL COLLEGE, (Id: C-12290)",
        "college_type": "Constituent / University College",
        "district": "Kanpur Nagar",
        "state": "Uttar Pradesh",
        "university": "Chatrapati Sahuji Maharaj Kanpur University, Kanpur (Id: U-0505)"
    },
    {
        "college_name": "College of Agricultural Engineering & Technology (Id: C-29457)",
        "college_type": "Constituent / University College",
        "district": "Hisar",
        "state": "Haryana",
        "university": "Chaudhary Charan Singh Haryana Agricultural University, Hisar (Id: U-0159)"
    },
    {
        "college_name": "College of Agriculture (Id: C-29453)",
        "college_type": "Constituent / University College",
        "district": "Hisar",
        "state": "Haryana",
        "university": "Chaudhary Charan Singh Haryana Agricultural University, Hisar (Id: U-0159)"
    },
    {
        "college_name": "College of Agriculture (Id: C-29456)",
        "college_type": "Constituent / University College",
        "district": "Kaithal",
        "state": "Haryana",
        "university": "Chaudhary Charan Singh Haryana Agricultural University, Hisar (Id: U-0159)"
    },
    {
        "college_name": "College of Basic Sciences & Humanities (Id: C-29455)",
        "college_type": "Constituent / University College",
        "district": "Hisar",
        "state": "Haryana",
        "university": "Chaudhary Charan Singh Haryana Agricultural University, Hisar (Id: U-0159)"
    },
    {
        "college_name": "I.C.College of Home Science (Id: C-29454)",
        "college_type": "Constituent / University College",
        "district": "Hisar",
        "state": "Haryana",
        "university": "Chaudhary Charan Singh Haryana Agricultural University, Hisar (Id: U-0159)"
    },
    {
        "college_name": "Chettinad College of Nursing (Id: C-7048)",
        "college_type": "Constituent / University College",
        "district": "Kancheepuram",
        "state": "Tamil Nadu",
        "university": "Chettinad Academy of Research & Education, Kancheepuram (Id: U-0451)"
    },
    {
        "college_name": "Chettinad Hospital and Research Institute (Id: C-7049)",
        "college_type": "Constituent / University College",
        "district": "Kancheepuram",
        "state": "Tamil Nadu",
        "university": "Chettinad Academy of Research & Education, Kancheepuram (Id: U-0451)"
    },
    {
        "college_name": "College of Dairy Technology (Id: C-33325)",
        "college_type": "Constituent / University College",
        "district": "Raipur",
        "state": "Chhatisgarh",
        "university": "CHHATTISGARH KAMDHENU VISHWAVIDALAYA (Id: U-0634)"
    },
    {
        "college_name": "College of Fisheries (Id: C-33324)",
        "college_type": "Constituent / University College",
        "district": "Kabeerdham",
        "state": "Chhatisgarh",
        "university": "CHHATTISGARH KAMDHENU VISHWAVIDALAYA (Id: U-0634)"
    },
    {
        "college_name": "College of Veterinary Science & Animal Husbandry (Id: C-33326)",
        "college_type": "Constituent / University College",
        "district": "Durg",
        "state": "Chhatisgarh",
        "university": "CHHATTISGARH KAMDHENU VISHWAVIDALAYA (Id: U-0634)"
    },
    {
        "college_name": "Chitkara College of Education for Women (Id: C-24711)",
        "college_type": "Constituent / University College",
        "district": "Patiala",
        "state": "Punjab",
        "university": "Chitkara University, Patiala (Id: U-0373)"
    },
    {
        "college_name": "Chitkara College of Pharmacy (Id: C-24709)",
        "college_type": "Constituent / University College",
        "district": "Patiala",
        "state": "Punjab",
        "university": "Chitkara University, Patiala (Id: U-0373)"
    },
    {
        "college_name": "Chitkara School of Planning & Architecture (Id: C-24712)",
        "college_type": "Constituent / University College",
        "district": "Patiala",
        "state": "Punjab",
        "university": "Chitkara University, Patiala (Id: U-0373)"
    },
    {
        "college_name": "Cochin University College of Engineering (Id: C-9476)",
        "college_type": "Constituent / University College",
        "district": "Alappuzha",
        "state": "Kerala",
        "university": "Cochin University of Science & Technology, Kochi (Id: U-0253)"
    },
    {
        "college_name": "Kunjali Marikkar School of Marine Engineering (Id: C-9469)",
        "college_type": "Constituent / University College",
        "district": "Ernakulam",
        "state": "Kerala",
        "university": "Cochin University of Science & Technology, Kochi (Id: U-0253)"
    },
    {
        "college_name": "School of Engineering (Id: C-9462)",
        "college_type": "Constituent / University College",
        "district": "Ernakulam",
        "state": "Kerala",
        "university": "Cochin University of Science & Technology, Kochi (Id: U-0253)"
    },
    {
        "college_name": "Jawaharlal Nehru Medical College (Id: C-35088)",
        "college_type": "Constituent / University College",
        "district": "Wardha",
        "state": "Maharashtra",
        "university": "Datta Meghe Institute of Medical Sciences, Nagpur (Id: U-0295)"
    },
    {
        "college_name": "Mahatma Gandhi Ayurved College, Hospital and Research Centre (Id: C-35092)",
        "college_type": "Constituent / University College",
        "district": "Wardha",
        "state": "Maharashtra",
        "university": "Datta Meghe Institute of Medical Sciences, Nagpur (Id: U-0295)"
    },
    {
        "college_name": "Ravi Nair Physiotherapy College (Id: C-35091)",
        "college_type": "Constituent / University College",
        "district": "Wardha",
        "state": "Maharashtra",
        "university": "Datta Meghe Institute of Medical Sciences, Nagpur (Id: U-0295)"
    },
    {
        "college_name": "Sharad Pawar Dental College (Id: C-35089)",
        "college_type": "Constituent / University College",
        "district": "Wardha",
        "state": "Maharashtra",
        "university": "Datta Meghe Institute of Medical Sciences, Nagpur (Id: U-0295)"
    },
    {
        "college_name": "Smt. Radhikabai Meghe Memorial College of Nursing (Id: C-35090)",
        "college_type": "Constituent / University College",
        "district": "Wardha",
        "state": "Maharashtra",
        "university": "Datta Meghe Institute of Medical Sciences, Nagpur (Id: U-0295)"
    },
    {
        "college_name": "Fine Arts College (Id: C-17711)",
        "college_type": "Constituent / University College",
        "district": "Davanagere",
        "state": "Karnataka",
        "university": "Davangere University, Davangere (Id: U-0218)"
    },
    {
        "college_name": "UBDT Engineering College (Id: C-17703)",
        "college_type": "Constituent / University College",
        "district": "Davanagere",
        "state": "Karnataka",
        "university": "Davangere University, Davangere (Id: U-0218)"
    },
    {
        "college_name": "DEI TECHNICAL COLLEGE (Id: C-12830)",
        "college_type": "Constituent / University College",
        "district": "Agra",
        "state": "Uttar Pradesh",
        "university": "Dayalbagh Educational Institute, Agra (Id: U-0507)"
    },
    {
        "college_name": "B.R.D. Medical College, Gorakhpur (Id: C-14117)",
        "college_type": "Constituent / University College",
        "district": "Gorakhpur",
        "state": "Uttar Pradesh",
        "university": "Deen Dayal Upadhyay Gorakhpur University, Gorakhpur (Id: U-0508)"
    },
    {
        "college_name": "College of Social Work , opp Dept. of Chemistry , Dr.Babasaheb Ambedkar Marathwada University Aurangabad. (Id: C-34403)",
        "college_type": "Constituent / University College",
        "district": "Aurangabad",
        "state": "Maharashtra",
        "university": "Dr. Babasaheb Ambedkar Marathwada University, Aurangabad (Id: U-0298)"
    },
    {
        "college_name": "Dr.Babasaheb Ambedkar Marathwada University Model College of Ghansawangi (Id: C-34559)",
        "college_type": "Constituent / University College",
        "district": "Jalna",
        "state": "Maharashtra",
        "university": "Dr. Babasaheb Ambedkar Marathwada University, Aurangabad (Id: U-0298)"
    },
    {
        "college_name": "College of Agricultural Engineering & Technology (Id: C-43582)",
        "college_type": "Constituent / University College",
        "district": "Ratnagiri",
        "state": "Maharashtra",
        "university": "Dr. Balasaheb Sawant Konkan Krishi Vidyaapeeth,(former Konkan Krishi Vidyapeeth) Ratnagiri (Id: U-0300)"
    },
    {
        "college_name": "College of Agriculture, Dapoli (Id: C-44805)",
        "college_type": "Constituent / University College",
        "district": "Ratnagiri",
        "state": "Maharashtra",
        "university": "Dr. Balasaheb Sawant Konkan Krishi Vidyaapeeth,(former Konkan Krishi Vidyapeeth) Ratnagiri (Id: U-0300)"
    },
    {
        "college_name": "College of Fisheries (Id: C-43575)",
        "college_type": "Constituent / University College",
        "district": "Ratnagiri",
        "state": "Maharashtra",
        "university": "Dr. Balasaheb Sawant Konkan Krishi Vidyaapeeth,(former Konkan Krishi Vidyapeeth) Ratnagiri (Id: U-0300)"
    },
    {
        "college_name": "College of Forestry (Id: C-43576)",
        "college_type": "Constituent / University College",
        "district": "Ratnagiri",
        "state": "Maharashtra",
        "university": "Dr. Balasaheb Sawant Konkan Krishi Vidyaapeeth,(former Konkan Krishi Vidyapeeth) Ratnagiri (Id: U-0300)"
    },
    {
        "college_name": "POST GRADUATE INSTITUTE OF POST HARVEST MANAGEMENT, KILLA-ROHA (Id: C-45861)",
        "college_type": "Constituent / University College",
        "district": "Raigarh",
        "state": "Maharashtra",
        "university": "Dr. Balasaheb Sawant Konkan Krishi Vidyaapeeth,(former Konkan Krishi Vidyapeeth) Ratnagiri (Id: U-0300)"
    },
    {
        "college_name": "Dr. D. Y. Patil Biotechnology and Bioinformatics Institute, Tathawade, Pune (Id: C-43240)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Dr. D.Y.Patil Vidyapeeth, Pune (Id: U-0301)"
    },
    {
        "college_name": "Dr. D. Y. Patil Dental College & Hospital, Pune (Id: C-43243)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Dr. D.Y.Patil Vidyapeeth, Pune (Id: U-0301)"
    },
    {
        "college_name": "Dr. D. Y. Patil Institute of Optometry and Visual Sciences, Pune (Id: C-43241)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Dr. D.Y.Patil Vidyapeeth, Pune (Id: U-0301)"
    },
    {
        "college_name": "Global Business School & Research Centre, Tathawade, Pune (Id: C-43238)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Dr. D.Y.Patil Vidyapeeth, Pune (Id: U-0301)"
    },
    {
        "college_name": "Institute of Distance Learning (Id: C-43245)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Dr. D.Y.Patil Vidyapeeth, Pune (Id: U-0301)"
    },
    {
        "college_name": "Padmashree Dr. D. Y. Patil College of Nursing, Pune (Id: C-43242)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Dr. D.Y.Patil Vidyapeeth, Pune (Id: U-0301)"
    },
    {
        "college_name": "Padmashree Dr. D. Y. Patil College of Physiotherapy, Pune (Id: C-43239)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Dr. D.Y.Patil Vidyapeeth, Pune (Id: U-0301)"
    },
    {
        "college_name": "Padmashree Dr. D. Y. Patil Medical College, Hospital and Research Centre, Pune (Id: C-43244)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Dr. D.Y.Patil Vidyapeeth, Pune (Id: U-0301)"
    },
    {
        "college_name": "A.B.M. COLLEGE NAGPUR (Id: C-44544)",
        "college_type": "Constituent / University College",
        "district": "Nagpur",
        "state": "Maharashtra",
        "university": "Dr. Punjarao Deshmukh Krishi Vidyapeeth, Akola (Id: U-0302)"
    },
    {
        "college_name": "COLLEGE OF AGRICULTURAL ENGINEERING & TECHNOLOGY, AKOLA (Id: C-44558)",
        "college_type": "Constituent / University College",
        "district": "Akola",
        "state": "Maharashtra",
        "university": "Dr. Punjarao Deshmukh Krishi Vidyapeeth, Akola (Id: U-0302)"
    },
    {
        "college_name": "COLLEGE OF AGRICULTURE, AKOLA (Id: C-44561)",
        "college_type": "Constituent / University College",
        "district": "Akola",
        "state": "Maharashtra",
        "university": "Dr. Punjarao Deshmukh Krishi Vidyapeeth, Akola (Id: U-0302)"
    },
    {
        "college_name": "COLLEGE OF AGRICULTURE, NAGPUR (Id: C-44556)",
        "college_type": "Constituent / University College",
        "district": "Nagpur",
        "state": "Maharashtra",
        "university": "Dr. Punjarao Deshmukh Krishi Vidyapeeth, Akola (Id: U-0302)"
    },
    {
        "college_name": "COLLEGE OF AGRICULTURE, SONAPUR (Id: C-44551)",
        "college_type": "Constituent / University College",
        "district": "Gadchiroli",
        "state": "Maharashtra",
        "university": "Dr. Punjarao Deshmukh Krishi Vidyapeeth, Akola (Id: U-0302)"
    },
    {
        "college_name": "COLLEGE OF FORESTRY (Id: C-44546)",
        "college_type": "Constituent / University College",
        "district": "Akola",
        "state": "Maharashtra",
        "university": "Dr. Punjarao Deshmukh Krishi Vidyapeeth, Akola (Id: U-0302)"
    },
    {
        "college_name": "COLLEGE OF HORTICULTURE, AKOLA (Id: C-44564)",
        "college_type": "Constituent / University College",
        "district": "Akola",
        "state": "Maharashtra",
        "university": "Dr. Punjarao Deshmukh Krishi Vidyapeeth, Akola (Id: U-0302)"
    },
    {
        "college_name": "POST GRADUATE INSTITUTE, AKOLA (Id: C-44566)",
        "college_type": "Constituent / University College",
        "district": "Akola",
        "state": "Maharashtra",
        "university": "Dr. Punjarao Deshmukh Krishi Vidyapeeth, Akola (Id: U-0302)"
    },
    {
        "college_name": "COLLEGE OF FORESTRY, SOLAN (Id: C-47458)",
        "college_type": "Constituent / University College",
        "district": "Solan",
        "state": "Himachal Pradesh",
        "university": "Dr. Y.S. Parmar University of Horticulture and Forestry, Solan (Id: U-0181)"
    },
    {
        "college_name": "College of Horticulture ( Main Campus) (Id: C-17666)",
        "college_type": "Constituent / University College",
        "district": "Solan",
        "state": "Himachal Pradesh",
        "university": "Dr. Y.S. Parmar University of Horticulture and Forestry, Solan (Id: U-0181)"
    },
    {
        "college_name": "Institute of Biotechnology and Environmental Sciences (Id: C-17665)",
        "college_type": "Constituent / University College",
        "district": "Hamirpur",
        "state": "Himachal Pradesh",
        "university": "Dr. Y.S. Parmar University of Horticulture and Forestry, Solan (Id: U-0181)"
    },
    {
        "college_name": "College of Horticultural/ Mojerla (Id: C-22057)",
        "college_type": "Constituent / University College",
        "district": "Mahbubnagar",
        "state": "Telangana",
        "university": "Dr Y S R Horticulture University (Id: U-0001)"
    },
    {
        "college_name": "College of Horticultural/ Rajendranagar (Id: C-22056)",
        "college_type": "Constituent / University College",
        "district": "Rangareddy",
        "state": "Telangana",
        "university": "Dr Y S R Horticulture University (Id: U-0001)"
    },
    {
        "college_name": "HCRI, Anantharajupet (Id: C-22055)",
        "college_type": "Constituent / University College",
        "district": "Y.S.R.",
        "state": "Andhra Pradesh",
        "university": "Dr Y S R Horticulture University (Id: U-0001)"
    },
    {
        "college_name": "HCRI, Venkataramannagudem (Id: C-22058)",
        "college_type": "Constituent / University College",
        "district": "West Godavari",
        "state": "Andhra Pradesh",
        "university": "Dr Y S R Horticulture University (Id: U-0001)"
    },
    {
        "college_name": "Medical College (Id: C-16170)",
        "college_type": "Constituent / University College",
        "district": "Kolhapur",
        "state": "Maharashtra",
        "university": "D.Y. Patil Educational Society , Kolhapur (Id: U-0294)"
    },
    {
        "college_name": "Nursing (Id: C-16168)",
        "college_type": "Constituent / University College",
        "district": "Kolhapur",
        "state": "Maharashtra",
        "university": "D.Y. Patil Educational Society , Kolhapur (Id: U-0294)"
    },
    {
        "college_name": "Physiotherapy (Id: C-16169)",
        "college_type": "Constituent / University College",
        "district": "Kolhapur",
        "state": "Maharashtra",
        "university": "D.Y. Patil Educational Society , Kolhapur (Id: U-0294)"
    },
    {
        "college_name": "Acharya Motibhai Patel Institute of Computer Studies (Id: C-448)",
        "college_type": "Constituent / University College",
        "district": "Mahesana",
        "state": "Gujarat",
        "university": "Ganpat Univeristy, Vidyanagar, Gandhinagar (Id: U-0132)"
    },
    {
        "college_name": "Mehsana Urban Institute of Biosciences (Id: C-447)",
        "college_type": "Constituent / University College",
        "district": "Mahesana",
        "state": "Gujarat",
        "university": "Ganpat Univeristy, Vidyanagar, Gandhinagar (Id: U-0132)"
    },
    {
        "college_name": "S.K. Patel College of Pharmaceutical Education & Research (Id: C-446)",
        "college_type": "Constituent / University College",
        "district": "Mahesana",
        "state": "Gujarat",
        "university": "Ganpat Univeristy, Vidyanagar, Gandhinagar (Id: U-0132)"
    },
    {
        "college_name": "U.V. Patel College of Engineering (Id: C-443)",
        "college_type": "Constituent / University College",
        "district": "Mahesana",
        "state": "Gujarat",
        "university": "Ganpat Univeristy, Vidyanagar, Gandhinagar (Id: U-0132)"
    },
    {
        "college_name": "V.M. Patel College of Management Studies (Id: C-442)",
        "college_type": "Constituent / University College",
        "district": "Mahesana",
        "state": "Gujarat",
        "university": "Ganpat Univeristy, Vidyanagar, Gandhinagar (Id: U-0132)"
    },
    {
        "college_name": "V.M. Patel Institute of Management (Id: C-445)",
        "college_type": "Constituent / University College",
        "district": "Mahesana",
        "state": "Gujarat",
        "university": "Ganpat Univeristy, Vidyanagar, Gandhinagar (Id: U-0132)"
    },
    {
        "college_name": "Gauhati University Law College (Id: C-17344)",
        "college_type": "Constituent / University College",
        "district": "Kamrup",
        "state": "Assam",
        "university": "Gauhati University, Guwahati (Id: U-0052)"
    },
    {
        "college_name": "School of Biotechnology (Id: C-44796)",
        "college_type": "Constituent / University College",
        "district": "Gautam Buddha Nagar",
        "state": "Uttar Pradesh",
        "university": "Gautam Buddha University, Greater Noida, Gautam Budh Nagar (Id: U-0514)"
    },
    {
        "college_name": "School of Buddhist Studies and Civilization (Id: C-44799)",
        "college_type": "Constituent / University College",
        "district": "Gautam Buddha Nagar",
        "state": "Uttar Pradesh",
        "university": "Gautam Buddha University, Greater Noida, Gautam Budh Nagar (Id: U-0514)"
    },
    {
        "college_name": "School of Engineering (Id: C-44795)",
        "college_type": "Constituent / University College",
        "district": "Gautam Buddha Nagar",
        "state": "Uttar Pradesh",
        "university": "Gautam Buddha University, Greater Noida, Gautam Budh Nagar (Id: U-0514)"
    },
    {
        "college_name": "School of Humanities and Social Science (Id: C-44794)",
        "college_type": "Constituent / University College",
        "district": "Gautam Buddha Nagar",
        "state": "Uttar Pradesh",
        "university": "Gautam Buddha University, Greater Noida, Gautam Budh Nagar (Id: U-0514)"
    },
    {
        "college_name": "School of Information and Communication Technology (Id: C-44793)",
        "college_type": "Constituent / University College",
        "district": "Gautam Buddha Nagar",
        "state": "Uttar Pradesh",
        "university": "Gautam Buddha University, Greater Noida, Gautam Budh Nagar (Id: U-0514)"
    },
    {
        "college_name": "School of Law Justice and Governance (Id: C-44797)",
        "college_type": "Constituent / University College",
        "district": "Gautam Buddha Nagar",
        "state": "Uttar Pradesh",
        "university": "Gautam Buddha University, Greater Noida, Gautam Budh Nagar (Id: U-0514)"
    },
    {
        "college_name": "School of Management (Id: C-44798)",
        "college_type": "Constituent / University College",
        "district": "Gautam Buddha Nagar",
        "state": "Uttar Pradesh",
        "university": "Gautam Buddha University, Greater Noida, Gautam Budh Nagar (Id: U-0514)"
    },
    {
        "college_name": "School of Vocational Studies and Applied Science (Id: C-44792)",
        "college_type": "Constituent / University College",
        "district": "Gautam Buddha Nagar",
        "state": "Uttar Pradesh",
        "university": "Gautam Buddha University, Greater Noida, Gautam Budh Nagar (Id: U-0514)"
    },
    {
        "college_name": "College of Agribusiness Management (Id: C-16665)",
        "college_type": "Constituent / University College",
        "district": "Udham Singh Nagar",
        "state": "Uttrakhand",
        "university": "G.B. Pant Universtiy of Agriculture and Technology, Pantnagar (Id: U-0554)"
    },
    {
        "college_name": "College of Agriculture (Id: C-16666)",
        "college_type": "Constituent / University College",
        "district": "Udham Singh Nagar",
        "state": "Uttrakhand",
        "university": "G.B. Pant Universtiy of Agriculture and Technology, Pantnagar (Id: U-0554)"
    },
    {
        "college_name": "College of Fisheries (Id: C-16668)",
        "college_type": "Constituent / University College",
        "district": "Udham Singh Nagar",
        "state": "Uttrakhand",
        "university": "G.B. Pant Universtiy of Agriculture and Technology, Pantnagar (Id: U-0554)"
    },
    {
        "college_name": "College of Home Science (Id: C-16672)",
        "college_type": "Constituent / University College",
        "district": "Udham Singh Nagar",
        "state": "Uttrakhand",
        "university": "G.B. Pant Universtiy of Agriculture and Technology, Pantnagar (Id: U-0554)"
    },
    {
        "college_name": "College of Post-Graduate Studies (Id: C-16671)",
        "college_type": "Constituent / University College",
        "district": "Udham Singh Nagar",
        "state": "Uttrakhand",
        "university": "G.B. Pant Universtiy of Agriculture and Technology, Pantnagar (Id: U-0554)"
    },
    {
        "college_name": "College of Technology (Id: C-16673)",
        "college_type": "Constituent / University College",
        "district": "Udham Singh Nagar",
        "state": "Uttrakhand",
        "university": "G.B. Pant Universtiy of Agriculture and Technology, Pantnagar (Id: U-0554)"
    },
    {
        "college_name": "College of Veterinary & Animal Sciences (Id: C-16667)",
        "college_type": "Constituent / University College",
        "district": "Udham Singh Nagar",
        "state": "Uttrakhand",
        "university": "G.B. Pant Universtiy of Agriculture and Technology, Pantnagar (Id: U-0554)"
    },
    {
        "college_name": "Colloge of Basic Sciences & Humanities (Id: C-16670)",
        "college_type": "Constituent / University College",
        "district": "Udham Singh Nagar",
        "state": "Uttrakhand",
        "university": "G.B. Pant Universtiy of Agriculture and Technology, Pantnagar (Id: U-0554)"
    },
    {
        "college_name": "Institute of Applied Science & Humanities (Id: C-21629)",
        "college_type": "Constituent / University College",
        "district": "Mathura",
        "state": "Uttar Pradesh",
        "university": "G.L.A University, Mathura (Id: U-0513)"
    },
    {
        "college_name": "Institute of Business Management (Id: C-21628)",
        "college_type": "Constituent / University College",
        "district": "Mathura",
        "state": "Uttar Pradesh",
        "university": "G.L.A University, Mathura (Id: U-0513)"
    },
    {
        "college_name": "Institute of Engineering & Technology (Id: C-21627)",
        "college_type": "Constituent / University College",
        "district": "Mathura",
        "state": "Uttar Pradesh",
        "university": "G.L.A University, Mathura (Id: U-0513)"
    },
    {
        "college_name": "Institute of Pharmaceutical Research (Id: C-21630)",
        "college_type": "Constituent / University College",
        "district": "Mathura",
        "state": "Uttar Pradesh",
        "university": "G.L.A University, Mathura (Id: U-0513)"
    },
    {
        "college_name": "Institute of Ayruvedic Pharmaceutical Sciences (Id: C-6438)",
        "college_type": "Constituent / University College",
        "district": "Jamnagar",
        "state": "Gujarat",
        "university": "Gujarat Ayurveda University, Jamnagar (Id: U-0133)"
    },
    {
        "college_name": "Maharshi Patanjali Institute for Yoga Naturopathy Education and Research (Id: C-6441)",
        "college_type": "Constituent / University College",
        "district": "Jamnagar",
        "state": "Gujarat",
        "university": "Gujarat Ayurveda University, Jamnagar (Id: U-0133)"
    },
    {
        "college_name": "Shri Gulab Kunvarba Ayurved College (Id: C-6434)",
        "college_type": "Constituent / University College",
        "district": "Jamnagar",
        "state": "Gujarat",
        "university": "Gujarat Ayurveda University, Jamnagar (Id: U-0133)"
    },
    {
        "college_name": "K. S. School of Business Management (Id: C-5808)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Gujarat University, Ahmedabad (Id: U-0136)"
    },
    {
        "college_name": "Hindi Shiksha Mahavidyalaya, Ahmedabad (Id: C-1070)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Gujarat Vidyapith, Ahmedabad (Id: U-0137)"
    },
    {
        "college_name": "Mahadev Desai College of Physical Education, Sadra (Id: C-1067)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Gujarat Vidyapith, Ahmedabad (Id: U-0137)"
    },
    {
        "college_name": "Mahadev Desai Gram Seva Mahavidyalaya (for Boys), Sadra (Id: C-1063)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Gujarat Vidyapith, Ahmedabad (Id: U-0137)"
    },
    {
        "college_name": "Mahadev Desai Gram Seva Mahavidyalaya (For Girls), Randheja (Id: C-1065)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Gujarat Vidyapith, Ahmedabad (Id: U-0137)"
    },
    {
        "college_name": "Mahadev Desai Samaj Seva Mahavidyalaya, Ahmedabad (Id: C-1068)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Gujarat Vidyapith, Ahmedabad (Id: U-0137)"
    },
    {
        "college_name": "Shikshan Mahavidyalaya (College of Education), Ahmedabad (Id: C-1064)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Gujarat Vidyapith, Ahmedabad (Id: U-0137)"
    },
    {
        "college_name": "University UG Programme for B.P.Ed. (Id: C-21633)",
        "college_type": "Constituent / University College",
        "district": "Gulbarga",
        "state": "Karnataka",
        "university": "Gulbarga University, Gulbarga (Id: U-0219)"
    },
    {
        "college_name": "College of Dairy Science & Technology (Id: C-453)",
        "college_type": "Constituent / University College",
        "district": "Ludhiana",
        "state": "Punjab",
        "university": "Guru Angad Dev Veterinary & Animal Sciences University, Ludhiana (Id: U-0375)"
    },
    {
        "college_name": "College of Fisheries (Id: C-452)",
        "college_type": "Constituent / University College",
        "district": "Ludhiana",
        "state": "Punjab",
        "university": "Guru Angad Dev Veterinary & Animal Sciences University, Ludhiana (Id: U-0375)"
    },
    {
        "college_name": "College of Veterinary Science (Id: C-451)",
        "college_type": "Constituent / University College",
        "district": "Ludhiana",
        "state": "Punjab",
        "university": "Guru Angad Dev Veterinary & Animal Sciences University, Ludhiana (Id: U-0375)"
    },
    {
        "college_name": "Polytechnic College (Id: C-454)",
        "college_type": "Constituent / University College",
        "district": "Bathinda",
        "state": "Punjab",
        "university": "Guru Angad Dev Veterinary & Animal Sciences University, Ludhiana (Id: U-0375)"
    },
    {
        "college_name": "School of Animal Biotechnology (Id: C-449)",
        "college_type": "Constituent / University College",
        "district": "Ludhiana",
        "state": "Punjab",
        "university": "Guru Angad Dev Veterinary & Animal Sciences University, Ludhiana (Id: U-0375)"
    },
    {
        "college_name": "Indira Gandhi Institute of Technology (Id: C-32915)",
        "college_type": "Constituent / University College",
        "district": "Central",
        "state": "Delhi",
        "university": "Guru Gobind Singh Indraprastha University (Id: U-0099)"
    },
    {
        "college_name": "ASSM College, Mukandpur (Id: C-27877)",
        "college_type": "Constituent / University College",
        "district": "Shahid Bhagat Singh Nagar",
        "state": "Punjab",
        "university": "Guru Nanak Dev University, Amritsar (Id: U-0376)"
    },
    {
        "college_name": "Bebe Nanki University College, Vill. Mithra (Id: C-27980)",
        "college_type": "Constituent / University College",
        "district": "Kapurthala",
        "state": "Punjab",
        "university": "Guru Nanak Dev University, Amritsar (Id: U-0376)"
    },
    {
        "college_name": "GND University College, Near Govt. College of Edu., Ladowali Rd. (Id: C-27988)",
        "college_type": "Constituent / University College",
        "district": "Jalandhar",
        "state": "Punjab",
        "university": "Guru Nanak Dev University, Amritsar (Id: U-0376)"
    },
    {
        "college_name": "Guru Nanak Dev University College, Chung, Khemkaran Road, Near Bhikhiwind (Id: C-27861)",
        "college_type": "Constituent / University College",
        "district": "Tarn Taran",
        "state": "Punjab",
        "university": "Guru Nanak Dev University, Amritsar (Id: U-0376)"
    },
    {
        "college_name": "Guru Nanak Dev University College, Narot Jaimal Singh (Id: C-27974)",
        "college_type": "Constituent / University College",
        "district": "Gurdaspur",
        "state": "Punjab",
        "university": "Guru Nanak Dev University, Amritsar (Id: U-0376)"
    },
    {
        "college_name": "Guru Nanak Dev University College, Verka (Id: C-27921)",
        "college_type": "Constituent / University College",
        "district": "Amritsar",
        "state": "Punjab",
        "university": "Guru Nanak Dev University, Amritsar (Id: U-0376)"
    },
    {
        "college_name": "Shaheed Ram Singh Pathania Memorial College, Niari Block Kalan (Id: C-27967)",
        "college_type": "Constituent / University College",
        "district": "Gurdaspur",
        "state": "Punjab",
        "university": "Guru Nanak Dev University, Amritsar (Id: U-0376)"
    },
    {
        "college_name": "Himalayan Institute of Medical Sciences (Id: C-10213)",
        "college_type": "Constituent / University College",
        "district": "Dehradun",
        "state": "Uttrakhand",
        "university": "HIHT University, Dehradun (Id: U-0558)"
    },
    {
        "college_name": "HPU Centre for Evening Studies, The Mall, Shimla (Id: C-11485)",
        "college_type": "Constituent / University College",
        "district": "Shimla",
        "state": "Himachal Pradesh",
        "university": "Himachal Pradesh University , Shimla (Id: U-0183)"
    },
    {
        "college_name": "HP University College of Business Studies, Ava Lodge, Shimla (Id: C-11258)",
        "college_type": "Constituent / University College",
        "district": "Shimla",
        "state": "Himachal Pradesh",
        "university": "Himachal Pradesh University , Shimla (Id: U-0183)"
    },
    {
        "college_name": "HP University Institute of Legal Studies, Ava Lodge, Shimla (Id: C-11413)",
        "college_type": "Constituent / University College",
        "district": "Shimla",
        "state": "Himachal Pradesh",
        "university": "Himachal Pradesh University , Shimla (Id: U-0183)"
    },
    {
        "college_name": "H.P. University Regional Centre, Dharamshala (Id: C-16675)",
        "college_type": "Constituent / University College",
        "district": "Kangra",
        "state": "Himachal Pradesh",
        "university": "Himachal Pradesh University , Shimla (Id: U-0183)"
    },
    {
        "college_name": "School Of Law, HPU, Regional Centre, Dharamshala (Id: C-16676)",
        "college_type": "Constituent / University College",
        "district": "Kangra",
        "state": "Himachal Pradesh",
        "university": "Himachal Pradesh University , Shimla (Id: U-0183)"
    },
    {
        "college_name": "University Institute of Information and Technology, H.P.U, Shimla (Id: C-11332)",
        "college_type": "Constituent / University College",
        "district": "Shimla",
        "state": "Himachal Pradesh",
        "university": "Himachal Pradesh University , Shimla (Id: U-0183)"
    },
    {
        "college_name": "Bhabha Atomic Research Centre (BARC), Mumbai (Id: C-39260)",
        "college_type": "Constituent / University College",
        "district": "Mumbai",
        "state": "Maharashtra",
        "university": "Homi Bhabha Natioanal Institute Knowledge Management Group, Mumbai (Id: U-0304)"
    },
    {
        "college_name": "Harish chandra Research Institute (HRI),Allahabad (Id: C-39253)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Homi Bhabha Natioanal Institute Knowledge Management Group, Mumbai (Id: U-0304)"
    },
    {
        "college_name": "Indira Gandhi Centre for Atomic Research (IGCAR), Kalpakkam (Id: C-39255)",
        "college_type": "Constituent / University College",
        "district": "Kancheepuram",
        "state": "Tamil Nadu",
        "university": "Homi Bhabha Natioanal Institute Knowledge Management Group, Mumbai (Id: U-0304)"
    },
    {
        "college_name": "Institute for Plasma Research (IPR),Gandhinagar (Id: C-39259)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Homi Bhabha Natioanal Institute Knowledge Management Group, Mumbai (Id: U-0304)"
    },
    {
        "college_name": "Institute of Physics (IOP),Bhubaneswar (Id: C-39258)",
        "college_type": "Constituent / University College",
        "district": "Cuttack",
        "state": "Odisha",
        "university": "Homi Bhabha Natioanal Institute Knowledge Management Group, Mumbai (Id: U-0304)"
    },
    {
        "college_name": "NATIONAL INSTITUTE OF SCIENCE EDUCATION AND RESEARCH (Id: C-45304)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Homi Bhabha Natioanal Institute Knowledge Management Group, Mumbai (Id: U-0304)"
    },
    {
        "college_name": "Raja Ramanna Centre for Advanced Technology (RRCAT),Indore (Id: C-39256)",
        "college_type": "Constituent / University College",
        "district": "Indore",
        "state": "Madhya Pradesh",
        "university": "Homi Bhabha Natioanal Institute Knowledge Management Group, Mumbai (Id: U-0304)"
    },
    {
        "college_name": "Saha Institute of Nuclear Physics (SINP),Kolkata (Id: C-39254)",
        "college_type": "Constituent / University College",
        "district": "Kolkata",
        "state": "West Bengal",
        "university": "Homi Bhabha Natioanal Institute Knowledge Management Group, Mumbai (Id: U-0304)"
    },
    {
        "college_name": "Tata Memorial Centre (TMC),Mumbai (Id: C-39257)",
        "college_type": "Constituent / University College",
        "district": "Mumbai",
        "state": "Maharashtra",
        "university": "Homi Bhabha Natioanal Institute Knowledge Management Group, Mumbai (Id: U-0304)"
    },
    {
        "college_name": "The Institute of Mathematical Sciences (IMSc),chennai (Id: C-39252)",
        "college_type": "Constituent / University College",
        "district": "Chennai",
        "state": "Tamil Nadu",
        "university": "Homi Bhabha Natioanal Institute Knowledge Management Group, Mumbai (Id: U-0304)"
    },
    {
        "college_name": "Variable Energy Cyclotron Centre (VECC),Kolkata (Id: C-39251)",
        "college_type": "Constituent / University College",
        "district": "Kolkata",
        "state": "West Bengal",
        "university": "Homi Bhabha Natioanal Institute Knowledge Management Group, Mumbai (Id: U-0304)"
    },
    {
        "college_name": "Dr. MPK Homoeopathic Medical College, Hospital & Research Centre (Id: C-16457)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "Homoeopathy University, Jaipur (Id: U-0607)"
    },
    {
        "college_name": "Faculty of Law (Id: C-43893)",
        "college_type": "Constituent / University College",
        "district": "Hyderabad",
        "state": "Telangana",
        "university": "ICFAI Foundation for Higher Education, Hyderabad (Id: U-0012)"
    },
    {
        "college_name": "Faculty of Science & Technology (Id: C-43894)",
        "college_type": "Constituent / University College",
        "district": "Hyderabad",
        "state": "Telangana",
        "university": "ICFAI Foundation for Higher Education, Hyderabad (Id: U-0012)"
    },
    {
        "college_name": "ICFAI Business School, Hyderabad (Faculty of Management) (Id: C-43895)",
        "college_type": "Constituent / University College",
        "district": "Hyderabad",
        "state": "Telangana",
        "university": "ICFAI Foundation for Higher Education, Hyderabad (Id: U-0012)"
    },
    {
        "college_name": "IGIMS College of Nursing Patna (Id: C-29462)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Indira Gandhi Institute of Medical Sciences, Patna (Id: U-0065)"
    },
    {
        "college_name": "Indira Gandhi Institute of Medical Sciences, Medical College Patna (Id: C-29463)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Indira Gandhi Institute of Medical Sciences, Patna (Id: U-0065)"
    },
    {
        "college_name": "BRSM College of Agricultural Engineering and Technology (Id: C-33316)",
        "college_type": "Constituent / University College",
        "district": "Bilaspur",
        "state": "Chhatisgarh",
        "university": "Indira Gandhi Krishi Vishwavidyalaya, Raipur (Id: U-0087)"
    },
    {
        "college_name": "College of Agriculture,Janjgir (Id: C-33322)",
        "college_type": "Constituent / University College",
        "district": "Janjgir - Champa",
        "state": "Chhatisgarh",
        "university": "Indira Gandhi Krishi Vishwavidyalaya, Raipur (Id: U-0087)"
    },
    {
        "college_name": "College of Agriculture,Raipur (Id: C-33321)",
        "college_type": "Constituent / University College",
        "district": "Raipur",
        "state": "Chhatisgarh",
        "university": "Indira Gandhi Krishi Vishwavidyalaya, Raipur (Id: U-0087)"
    },
    {
        "college_name": "College of Horticulture,Rajnandgaon (Id: C-33327)",
        "college_type": "Constituent / University College",
        "district": "Rajnandgaon",
        "state": "Chhatisgarh",
        "university": "Indira Gandhi Krishi Vishwavidyalaya, Raipur (Id: U-0087)"
    },
    {
        "college_name": "DKS COLLEGE OF AGRICULTURE AND RESEARCH STATION, BHATAPARA (Id: C-48334)",
        "college_type": "Constituent / University College",
        "district": "Raipur",
        "state": "Chhatisgarh",
        "university": "Indira Gandhi Krishi Vishwavidyalaya, Raipur (Id: U-0087)"
    },
    {
        "college_name": "Faculty of Agricultural Engineering (Id: C-33323)",
        "college_type": "Constituent / University College",
        "district": "Raipur",
        "state": "Chhatisgarh",
        "university": "Indira Gandhi Krishi Vishwavidyalaya, Raipur (Id: U-0087)"
    },
    {
        "college_name": "RMD College of Agriculture and Research Centre (Id: C-33297)",
        "college_type": "Constituent / University College",
        "district": "Surguja",
        "state": "Chhatisgarh",
        "university": "Indira Gandhi Krishi Vishwavidyalaya, Raipur (Id: U-0087)"
    },
    {
        "college_name": "SG College of Agriculture and Research Centre (Id: C-33320)",
        "college_type": "Constituent / University College",
        "district": "Bastar",
        "state": "Chhatisgarh",
        "university": "Indira Gandhi Krishi Vishwavidyalaya, Raipur (Id: U-0087)"
    },
    {
        "college_name": "SK College of Agriculture and Research Centre (Id: C-33318)",
        "college_type": "Constituent / University College",
        "district": "Kabeerdham",
        "state": "Chhatisgarh",
        "university": "Indira Gandhi Krishi Vishwavidyalaya, Raipur (Id: U-0087)"
    },
    {
        "college_name": "TCB College of Agriculture and Research Centre (Id: C-33315)",
        "college_type": "Constituent / University College",
        "district": "Bilaspur",
        "state": "Chhatisgarh",
        "university": "Indira Gandhi Krishi Vishwavidyalaya, Raipur (Id: U-0087)"
    },
    {
        "college_name": "INDUS INSTITUTE OF TECHNOLOGY & ENGINEERING (Id: C-47876)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "INDUS UNIVERSITY (Id: U-0663)"
    },
    {
        "college_name": "INSTITUTE OF AVIATION TECHNOLOGY AND ENGINEERING (Id: C-47380)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "INDUS UNIVERSITY (Id: U-0663)"
    },
    {
        "college_name": "INSTITUTE OF DESIGN ENVIRONMENT AND ARCHITECTURE (Id: C-47379)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "INDUS UNIVERSITY (Id: U-0663)"
    },
    {
        "college_name": "INSTITUTE OF INFORMATION AND COMMUNICATION TECHNOLOGY (Id: C-47381)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "INDUS UNIVERSITY (Id: U-0663)"
    },
    {
        "college_name": "Invertis Institute of Engineering & Technology (Id: C-12028)",
        "college_type": "Constituent / University College",
        "district": "Bareilly",
        "state": "Uttar Pradesh",
        "university": "Invertis University, Bareily (Id: U-0520)"
    },
    {
        "college_name": "Invertis Institute of Management Studies (Id: C-12029)",
        "college_type": "Constituent / University College",
        "district": "Bareilly",
        "state": "Uttar Pradesh",
        "university": "Invertis University, Bareily (Id: U-0520)"
    },
    {
        "college_name": "JSS College of Pharmacy (Id: C-35007)",
        "college_type": "Constituent / University College",
        "district": "Mysore",
        "state": "Karnataka",
        "university": "Jagadguru Sri Shivarathreeswara University, Mysore (Id: U-0222)"
    },
    {
        "college_name": "JSS College of Pharmacy (Id: C-35006)",
        "college_type": "Constituent / University College",
        "district": "The Nilgiris",
        "state": "Tamil Nadu",
        "university": "Jagadguru Sri Shivarathreeswara University, Mysore (Id: U-0222)"
    },
    {
        "college_name": "JSS Dental College and Hospital (Id: C-35008)",
        "college_type": "Constituent / University College",
        "district": "Mysore",
        "state": "Karnataka",
        "university": "Jagadguru Sri Shivarathreeswara University, Mysore (Id: U-0222)"
    },
    {
        "college_name": "JSS Medical College, Mysore (Id: C-35009)",
        "college_type": "Constituent / University College",
        "district": "Mysore",
        "state": "Karnataka",
        "university": "Jagadguru Sri Shivarathreeswara University, Mysore (Id: U-0222)"
    },
    {
        "college_name": "Acharya Kalu Kanya Mahavidyalaya (Id: C-22472)",
        "college_type": "Constituent / University College",
        "district": "Nagaur",
        "state": "Rajasthan",
        "university": "Jain Vishva Bharati Institute, Nagaur (Id: U-0400)"
    },
    {
        "college_name": "Bhola Prasad singh College, Bhore (Id: C-6488)",
        "college_type": "Constituent / University College",
        "district": "Gopalganj",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Dayanand Anglo Vedic Collge,Siwan (Id: C-7961)",
        "college_type": "Constituent / University College",
        "district": "Siwan",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Ganga Singh College, Chapra (Id: C-6458)",
        "college_type": "Constituent / University College",
        "district": "Saran",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Gopeshwar College,Hathua (Id: C-19496)",
        "college_type": "Constituent / University College",
        "district": "Gopalganj",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Hari Ram College, Mairwa (Id: C-19498)",
        "college_type": "Constituent / University College",
        "district": "Siwan",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Hotilal Ramnath College, Amnour (Id: C-6461)",
        "college_type": "Constituent / University College",
        "district": "Saran",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Jagdam College, Chapra (Id: C-6465)",
        "college_type": "Constituent / University College",
        "district": "Saran",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Jaglal Chaudhary College, Chapra (Id: C-6476)",
        "college_type": "Constituent / University College",
        "district": "Saran",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Jai Prakash Mahila College, Chapra (Id: C-6491)",
        "college_type": "Constituent / University College",
        "district": "Saran",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Kamla Rai College, Gopalganj (Id: C-19492)",
        "college_type": "Constituent / University College",
        "district": "Gopalganj",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Mahendra Mahila College, Gopalganj (Id: C-6454)",
        "college_type": "Constituent / University College",
        "district": "Gopalganj",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Nand Lal Singh College, Daudpur (Id: C-6464)",
        "college_type": "Constituent / University College",
        "district": "Saran",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Narayan College Goreya Kothi (Id: C-7958)",
        "college_type": "Constituent / University College",
        "district": "Siwan",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Prabhu Nath College, Parsa (Id: C-19499)",
        "college_type": "Constituent / University College",
        "district": "Saran",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Prithwi Chand Vigyan College, Chapra (Id: C-6459)",
        "college_type": "Constituent / University College",
        "district": "Saran",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Raja Singh College, Siwan (Id: C-6479)",
        "college_type": "Constituent / University College",
        "district": "Siwan",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Rajendra College, Chapra (Id: C-6487)",
        "college_type": "Constituent / University College",
        "district": "Saran",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Ram Bilas Ganga Ram College, Maharajganj (Id: C-6480)",
        "college_type": "Constituent / University College",
        "district": "Siwan",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Ram Jaipal College, Chapra (Id: C-6489)",
        "college_type": "Constituent / University College",
        "district": "Saran",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Vidya Bhawan Mahila College,Siwan (Id: C-7969)",
        "college_type": "Constituent / University College",
        "district": "Siwan",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "Yadunandan College, Dighwara (Id: C-6486)",
        "college_type": "Constituent / University College",
        "district": "Saran",
        "state": "Bihar",
        "university": "Jai Prakash Vishwavidyalaya, Chapra (Id: U-0066)"
    },
    {
        "college_name": "College of Agricultural Engineering, Jabalpur (Id: C-29470)",
        "college_type": "Constituent / University College",
        "district": "Jabalpur",
        "state": "Madhya Pradesh",
        "university": "Jawaharlal Nehru Krishi Vishwavidyalaya, Jabalpur (Id: U-0274)"
    },
    {
        "college_name": "College of Agriculture, Ganjbasoda (Id: C-29469)",
        "college_type": "Constituent / University College",
        "district": "Vidisha",
        "state": "Madhya Pradesh",
        "university": "Jawaharlal Nehru Krishi Vishwavidyalaya, Jabalpur (Id: U-0274)"
    },
    {
        "college_name": "College of Agriculture, Jabalpur (Id: C-29472)",
        "college_type": "Constituent / University College",
        "district": "Jabalpur",
        "state": "Madhya Pradesh",
        "university": "Jawaharlal Nehru Krishi Vishwavidyalaya, Jabalpur (Id: U-0274)"
    },
    {
        "college_name": "College of Agriculture , Rewa (Id: C-29473)",
        "college_type": "Constituent / University College",
        "district": "Rewa",
        "state": "Madhya Pradesh",
        "university": "Jawaharlal Nehru Krishi Vishwavidyalaya, Jabalpur (Id: U-0274)"
    },
    {
        "college_name": "College of Agriculture, Tikamgarh (Id: C-29471)",
        "college_type": "Constituent / University College",
        "district": "Tikamgarh",
        "state": "Madhya Pradesh",
        "university": "Jawaharlal Nehru Krishi Vishwavidyalaya, Jabalpur (Id: U-0274)"
    },
    {
        "college_name": "College of Agriculture, Warasiwani (Id: C-47403)",
        "college_type": "Constituent / University College",
        "district": "Balaghat",
        "state": "Madhya Pradesh",
        "university": "Jawaharlal Nehru Krishi Vishwavidyalaya, Jabalpur (Id: U-0274)"
    },
    {
        "college_name": "JNTUA College of Engineering, Anantapur (Id: C-26928)",
        "college_type": "Constituent / University College",
        "district": "Anantapur",
        "state": "Andhra Pradesh",
        "university": "Jawaharlal Nehru Technological University, Anantapur (Id: U-0016)"
    },
    {
        "college_name": "JNTUA College of Engineering, Pulivendula (Id: C-26847)",
        "college_type": "Constituent / University College",
        "district": "Y.S.R.",
        "state": "Andhra Pradesh",
        "university": "Jawaharlal Nehru Technological University, Anantapur (Id: U-0016)"
    },
    {
        "college_name": "JNTUA MBA, Anantapur (Id: C-26865)",
        "college_type": "Constituent / University College",
        "district": "Anantapur",
        "state": "Andhra Pradesh",
        "university": "Jawaharlal Nehru Technological University, Anantapur (Id: U-0016)"
    },
    {
        "college_name": "JNTUA-Oil Technological Research Center (Id: C-26966)",
        "college_type": "Constituent / University College",
        "district": "Anantapur",
        "state": "Andhra Pradesh",
        "university": "Jawaharlal Nehru Technological University, Anantapur (Id: U-0016)"
    },
    {
        "college_name": "JNTUH College of Engineering Hyderabad (Id: C-19913)",
        "college_type": "Constituent / University College",
        "district": "Hyderabad",
        "state": "Telangana",
        "university": "Jawaharlal Nehru Technological University, Hyderabad (Id: U-0017)"
    },
    {
        "college_name": "JNTUH College of Engineering Jagityala (Id: C-19872)",
        "college_type": "Constituent / University College",
        "district": "Karimnagar",
        "state": "Telangana",
        "university": "Jawaharlal Nehru Technological University, Hyderabad (Id: U-0017)"
    },
    {
        "college_name": "JNTUH College of Engineering Manthani (Id: C-19808)",
        "college_type": "Constituent / University College",
        "district": "Karimnagar",
        "state": "Telangana",
        "university": "Jawaharlal Nehru Technological University, Hyderabad (Id: U-0017)"
    },
    {
        "college_name": "University College of Engineering, Kakinada (AUTONOMOUS) (Id: C-18154)",
        "college_type": "Constituent / University College",
        "district": "East Godavari",
        "state": "Andhra Pradesh",
        "university": "Jawaharlal Nehru Technological University, Kakinada (Id: U-0015)"
    },
    {
        "college_name": "University College of Engineering, Vizianagaram (Id: C-17902)",
        "college_type": "Constituent / University College",
        "district": "Vizianagaram",
        "state": "Andhra Pradesh",
        "university": "Jawaharlal Nehru Technological University, Kakinada (Id: U-0015)"
    },
    {
        "college_name": "COLLEGE OF FINE ARTS (Id: C-17028)",
        "college_type": "Constituent / University College",
        "district": "Rangareddy",
        "state": "Telangana",
        "university": "Jawarharlal Nehru Architecture and Fine Art University Hyderabad (Id: U-0018)"
    },
    {
        "college_name": "SCHOOL OF PLANNING AND ARCHTECTURE (Id: C-17029)",
        "college_type": "Constituent / University College",
        "district": "Rangareddy",
        "state": "Telangana",
        "university": "Jawarharlal Nehru Architecture and Fine Art University Hyderabad (Id: U-0018)"
    },
    {
        "college_name": "Faculty of Applied Sciences (Id: C-44614)",
        "college_type": "Constituent / University College",
        "district": "Jodhpur",
        "state": "Rajasthan",
        "university": "Jodhpur National University, Jodhpur (Id: U-0403)"
    },
    {
        "college_name": "Faculty of Computer Application (Id: C-44612)",
        "college_type": "Constituent / University College",
        "district": "Jodhpur",
        "state": "Rajasthan",
        "university": "Jodhpur National University, Jodhpur (Id: U-0403)"
    },
    {
        "college_name": "Faculty of Education (Id: C-44613)",
        "college_type": "Constituent / University College",
        "district": "Jodhpur",
        "state": "Rajasthan",
        "university": "Jodhpur National University, Jodhpur (Id: U-0403)"
    },
    {
        "college_name": "Faculty of Engineering and Technology (Id: C-44611)",
        "college_type": "Constituent / University College",
        "district": "Jodhpur",
        "state": "Rajasthan",
        "university": "Jodhpur National University, Jodhpur (Id: U-0403)"
    },
    {
        "college_name": "Faculty of Law (Id: C-44609)",
        "college_type": "Constituent / University College",
        "district": "Jodhpur",
        "state": "Rajasthan",
        "university": "Jodhpur National University, Jodhpur (Id: U-0403)"
    },
    {
        "college_name": "Faculty of Management (Id: C-44615)",
        "college_type": "Constituent / University College",
        "district": "Jodhpur",
        "state": "Rajasthan",
        "university": "Jodhpur National University, Jodhpur (Id: U-0403)"
    },
    {
        "college_name": "Faculty of Medicine and Health (Id: C-44610)",
        "college_type": "Constituent / University College",
        "district": "Jodhpur",
        "state": "Rajasthan",
        "university": "Jodhpur National University, Jodhpur (Id: U-0403)"
    },
    {
        "college_name": "Faculty of Pharmaceutical Sciences (Id: C-44608)",
        "college_type": "Constituent / University College",
        "district": "Jodhpur",
        "state": "Rajasthan",
        "university": "Jodhpur National University, Jodhpur (Id: U-0403)"
    },
    {
        "college_name": "College of Agricultural Engineering and Technology- Junagadh (Id: C-6352)",
        "college_type": "Constituent / University College",
        "district": "Junagadh",
        "state": "Gujarat",
        "university": "Junagadh Agricultural University (Id: U-0140)"
    },
    {
        "college_name": "College of Agriculture - Junagadh (Id: C-6351)",
        "college_type": "Constituent / University College",
        "district": "Junagadh",
        "state": "Gujarat",
        "university": "Junagadh Agricultural University (Id: U-0140)"
    },
    {
        "college_name": "College of Fisheries Sciences- Veraval (Id: C-6346)",
        "college_type": "Constituent / University College",
        "district": "Junagadh",
        "state": "Gujarat",
        "university": "Junagadh Agricultural University (Id: U-0140)"
    },
    {
        "college_name": "College of Veterinary Science and Animal Husbandary- Junagadh (Id: C-6345)",
        "college_type": "Constituent / University College",
        "district": "Junagadh",
        "state": "Gujarat",
        "university": "Junagadh Agricultural University (Id: U-0140)"
    },
    {
        "college_name": "030 L.D.R.P. INSTITUTE OF TECH. & RESEARCH., GANDHINAGAR (Id: C-322)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "521 Leelaben Dashrathbhai Ramdas Patel Institute of Technology & Research (SFI)-Gandhinagar (Id: C-341)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "528 S V Institute of Computer Studies(SFI),KADI. (Id: C-379)",
        "college_type": "Constituent / University College",
        "district": "Mahesana",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "732 Leelaben Dashrathbhai Rramdas Patel Institute of Technology & Research (SFI) Gandhinagar (Id: C-222)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "749 S.V. Institute of Management (SFI),Kadi. (Id: C-375)",
        "college_type": "Constituent / University College",
        "district": "Mahesana",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "ASHVINBHAI A PATEL COMMERCE COLLEGE (Id: C-1082)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "B P COLLEGE OF BUSINESS ADMINISTRATION (Id: C-1074)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "B P COLLEGE OF COMPUTER STUDIES (Id: C-1080)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "CHANCHALBEN MAFATLAL PATEL COLLEGE OF NURSING (Id: C-1075)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "K B INSTITUTE OF PHARMACEUTICAL EDUCATION AND RESEARCH (Id: C-1078)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "R H PATEL ENGLISH MEDIUM B ED COLLEGE (Id: C-1076)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "SARVA VIDHYALAYA MED COLLEGE KADI (Id: C-6872)",
        "college_type": "Constituent / University College",
        "district": "Mahesana",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "S K PATEL INSTITUTE OF MANAGEMENT AND COMPUTER STUDIES (Id: C-1081)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "SOORAJBA COLLEGE OF EDUCATION (Id: C-1079)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "S S PATEL COLLEGE OF EDUCATION (Id: C-1077)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "S V COLLEGE OF EDUCATION KADI (Id: C-6902)",
        "college_type": "Constituent / University College",
        "district": "Mahesana",
        "state": "Gujarat",
        "university": "Kadi Sarva Vishwavidyalaya, Gandihnagar (Id: U-0141)"
    },
    {
        "college_name": "University Arts &Science College ,Subedari,Hanamkonda (Id: C-27223)",
        "college_type": "Constituent / University College",
        "district": "Warangal",
        "state": "Telangana",
        "university": "Kakatiya University, Warangal (Id: U-0019)"
    },
    {
        "college_name": "University college of Engineering,Kothagudam (Id: C-27616)",
        "college_type": "Constituent / University College",
        "district": "Khammam",
        "state": "Telangana",
        "university": "Kakatiya University, Warangal (Id: U-0019)"
    },
    {
        "college_name": "University Law college (Id: C-27614)",
        "college_type": "Constituent / University College",
        "district": "Warangal",
        "state": "Telangana",
        "university": "Kakatiya University, Warangal (Id: U-0019)"
    },
    {
        "college_name": "University P.G. College, Khammam (Id: C-32593)",
        "college_type": "Constituent / University College",
        "district": "Khammam",
        "state": "Telangana",
        "university": "Kakatiya University, Warangal (Id: U-0019)"
    },
    {
        "college_name": "University P.G. College, Nirmal (Id: C-32592)",
        "college_type": "Constituent / University College",
        "district": "Adilabad",
        "state": "Telangana",
        "university": "Kakatiya University, Warangal (Id: U-0019)"
    },
    {
        "college_name": "University P.G. College, Subedari,Hanamkonda (Id: C-32594)",
        "college_type": "Constituent / University College",
        "district": "Warangal",
        "state": "Telangana",
        "university": "Kakatiya University, Warangal (Id: U-0019)"
    },
    {
        "college_name": "Union Christian Training College (Id: C-7051)",
        "college_type": "Constituent / University College",
        "district": "Murshidabad",
        "state": "West Bengal",
        "university": "Kalyani University, Kalyani (Id: U-0576)"
    },
    {
        "college_name": "Adinath Parash Mani Skt. College, Rahua Sangram, Madhubani (Id: C-9619)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Akhil Bharatiye Skt. Hindi Vidypeeth, Khamhar, Begusarai (Id: C-9666)",
        "college_type": "Constituent / University College",
        "district": "Begusarai",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Awadh Bihari Sanskrit College, Rahimpur, Khagaria (Id: C-9634)",
        "college_type": "Constituent / University College",
        "district": "Khagaria",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Baba Sahib Ram Sanskrit College, Pacharhi, Darbhanga (Id: C-9673)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Baidyanath Pandey Arya Sanskrit College, Siwan (Id: C-9672)",
        "college_type": "Constituent / University College",
        "district": "Siwan",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Bharat Mishra Sanskrit College, Chapra (Id: C-9632)",
        "college_type": "Constituent / University College",
        "district": "Saran",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Brajbhushan Sanskrit College, Kharkhura, Gaya (Id: C-9641)",
        "college_type": "Constituent / University College",
        "district": "Gaya",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Dharma Samaj Sanskrit College, Muzaffarpur (Id: C-9658)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Government Sanskrit College, Bhagalpur (Id: C-9662)",
        "college_type": "Constituent / University College",
        "district": "Bhagalpur",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Government Sanskrit College, Kajipur, Patna (Id: C-9667)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Jagdamba Sanskrit College, Batho, Darbhanga (Id: C-9633)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Kalyani Mithila Sanskrit College, Deep, Madhubani (Id: C-9630)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "L.N.R. Sanskrit College, Jaideopatti, Darbhanga (Id: C-9617)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "L P N Sanskrit College, Baunsi, Banka (Id: C-9626)",
        "college_type": "Constituent / University College",
        "district": "Banka",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Madaneshwarnath Sanskrit College, Madaneshwar Asthan, Madhubani (Id: C-9660)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Mahanth Keshaw Sanskrit College, Fathuha, Patna (Id: C-9640)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "M.A.Rameshwar Lata Sanskrit College, Darbhanga (Id: C-9614)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "M.M. Lata Sanskrit Vidyapeeth, Lohana, Madhubani (Id: C-9659)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Nagarjun Umesh Sanskrit College, Tarauni, Darbhanga (Id: C-9645)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Nandan Sanskrit College, Ishahpur, Madhubani (Id: C-9652)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Nimbark Krishna Madhawanand Skt. College, Dhanamath, Patna (Id: C-9627)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Purnima Ram Pratap Sanskrit College, Baigani, Darbhanga (Id: C-9642)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Radha Umakant Sanskrit College, Sukhsena, Purnea (Id: C-9637)",
        "college_type": "Constituent / University College",
        "district": "Saharsa",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Raghavendra Sanskrit College, Taretpali, Naubatpur, Patna (Id: C-9663)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Ramadhin Mishra Bhaskaroday Sanskrit College, Deorahia, Buxar (Id: C-9624)",
        "college_type": "Constituent / University College",
        "district": "Buxar",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Ramautar Goutam Sanskrit College, Ahilya Asthan, (Id: C-9616)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Rishikul Br. Sanskrit College, Bediban Madhuban, West Champ. (Id: C-9613)",
        "college_type": "Constituent / University College",
        "district": "Pashchim Champaran",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Shiv Prasad Sanskrit Degree College, Rampur, Buxar (Id: C-9656)",
        "college_type": "Constituent / University College",
        "district": "Buxar",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Shri Ram Sanskrit College, Vijayeepur, Gopalganj (Id: C-9646)",
        "college_type": "Constituent / University College",
        "district": "Gopalganj",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Sidheshwari Sanskrit College, Pachrukhiya, Bhojpur (Id: C-9655)",
        "college_type": "Constituent / University College",
        "district": "Bhojpur",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Ugra Tara Bharati Mandan Sanskrit College, Mahishi, Saharsa (Id: C-9664)",
        "college_type": "Constituent / University College",
        "district": "Saharsa",
        "state": "Bihar",
        "university": "Kameshwar Singh Darbhanga Sanskrit Vishwavidyalaya, Darbhanga (Id: U-0067)"
    },
    {
        "college_name": "Maharaja Samskrita College, Mysore (Id: C-13487)",
        "college_type": "Constituent / University College",
        "district": "Mysore",
        "state": "Karnataka",
        "university": "Karnataka Sanskrit University (Id: U-0625)"
    },
    {
        "college_name": "Sri Chamarajendra Samskrita College, Bangalore (Id: C-13497)",
        "college_type": "Constituent / University College",
        "district": "Bangalore",
        "state": "Karnataka",
        "university": "Karnataka Sanskrit University (Id: U-0625)"
    },
    {
        "college_name": "KSLU the School of Law (Id: C-9813)",
        "college_type": "Constituent / University College",
        "district": "Dharwad",
        "state": "Karnataka",
        "university": "Karnataka State Law University, Hubli (Id: U-0227)"
    },
    {
        "college_name": "Karnataka Arts and Commerce College, Dharwad (Id: C-35702)",
        "college_type": "Constituent / University College",
        "district": "Dharwad",
        "state": "Karnataka",
        "university": "Karnataka University, Dharwad (Id: U-0230)"
    },
    {
        "college_name": "Karnataka Education College, Dharwad (Id: C-35461)",
        "college_type": "Constituent / University College",
        "district": "Dharwad",
        "state": "Karnataka",
        "university": "Karnataka University, Dharwad (Id: U-0230)"
    },
    {
        "college_name": "Karnataka Law College, Dharwad (Id: C-35528)",
        "college_type": "Constituent / University College",
        "district": "Dharwad",
        "state": "Karnataka",
        "university": "Karnataka University, Dharwad (Id: U-0230)"
    },
    {
        "college_name": "Karnataka Music College, Dharwad (Id: C-35520)",
        "college_type": "Constituent / University College",
        "district": "Dharwad",
        "state": "Karnataka",
        "university": "Karnataka University, Dharwad (Id: U-0230)"
    },
    {
        "college_name": "Karnataka Science College, Dharwad (Id: C-35555)",
        "college_type": "Constituent / University College",
        "district": "Dharwad",
        "state": "Karnataka",
        "university": "Karnataka University, Dharwad (Id: U-0230)"
    },
    {
        "college_name": "College of Fisheries, Mangalore (Id: C-30195)",
        "college_type": "Constituent / University College",
        "district": "Dakshina Kannada",
        "state": "Karnataka",
        "university": "Karnataka Vetrinary, Animal & Fisheries Science University, Nandinagar (Id: U-0231)"
    },
    {
        "college_name": "Dairy Science College, Bangalore (Id: C-30193)",
        "college_type": "Constituent / University College",
        "district": "Bangalore",
        "state": "Karnataka",
        "university": "Karnataka Vetrinary, Animal & Fisheries Science University, Nandinagar (Id: U-0231)"
    },
    {
        "college_name": "Dairy Science College, Mahagoan (Id: C-30192)",
        "college_type": "Constituent / University College",
        "district": "Gulbarga",
        "state": "Karnataka",
        "university": "Karnataka Vetrinary, Animal & Fisheries Science University, Nandinagar (Id: U-0231)"
    },
    {
        "college_name": "Veterinary College,Bangalore (Id: C-30190)",
        "college_type": "Constituent / University College",
        "district": "Bangalore",
        "state": "Karnataka",
        "university": "Karnataka Vetrinary, Animal & Fisheries Science University, Nandinagar (Id: U-0231)"
    },
    {
        "college_name": "Veterinary College, Bidar (Id: C-30194)",
        "college_type": "Constituent / University College",
        "district": "Bidar",
        "state": "Karnataka",
        "university": "Karnataka Vetrinary, Animal & Fisheries Science University, Nandinagar (Id: U-0231)"
    },
    {
        "college_name": "Veterinary College, Hassan (Id: C-30196)",
        "college_type": "Constituent / University College",
        "district": "Hassan",
        "state": "Karnataka",
        "university": "Karnataka Vetrinary, Animal & Fisheries Science University, Nandinagar (Id: U-0231)"
    },
    {
        "college_name": "Veterinary College, Shimoga (Id: C-30191)",
        "college_type": "Constituent / University College",
        "district": "Shimoga",
        "state": "Karnataka",
        "university": "Karnataka Vetrinary, Animal & Fisheries Science University, Nandinagar (Id: U-0231)"
    },
    {
        "college_name": "Kalidas Univerities B.Ed. Collage, Nagpur (Id: C-16267)",
        "college_type": "Constituent / University College",
        "district": "Nagpur",
        "state": "Maharashtra",
        "university": "Kavi Kulguru Kalidas Sanskrit Vishwavidyalaya, Ramtek (Id: U-0310)"
    },
    {
        "college_name": "College of Agriculture, Padannakkad (Id: C-44034)",
        "college_type": "Constituent / University College",
        "district": "Kasaragod",
        "state": "Kerala",
        "university": "Kerala Agricultural University, Thrissur (Id: U-0257)"
    },
    {
        "college_name": "College of Agriculture, Vellayanai (Id: C-44029)",
        "college_type": "Constituent / University College",
        "district": "Thiruvananthapuram",
        "state": "Kerala",
        "university": "Kerala Agricultural University, Thrissur (Id: U-0257)"
    },
    {
        "college_name": "College of Co-Operation Banking & Management, Vellanikkara (Id: C-44889)",
        "college_type": "Constituent / University College",
        "district": "Thrissur",
        "state": "Kerala",
        "university": "Kerala Agricultural University, Thrissur (Id: U-0257)"
    },
    {
        "college_name": "College of Forestry, Vellanikkara (Id: C-44033)",
        "college_type": "Constituent / University College",
        "district": "Thrissur",
        "state": "Kerala",
        "university": "Kerala Agricultural University, Thrissur (Id: U-0257)"
    },
    {
        "college_name": "College of Horticulture, Vellanikkara (Id: C-44031)",
        "college_type": "Constituent / University College",
        "district": "Thrissur",
        "state": "Kerala",
        "university": "Kerala Agricultural University, Thrissur (Id: U-0257)"
    },
    {
        "college_name": "Kelappaji College of Agrl. Engineering & Technology, Tavanur (Id: C-44030)",
        "college_type": "Constituent / University College",
        "district": "Malappuram",
        "state": "Kerala",
        "university": "Kerala Agricultural University, Thrissur (Id: U-0257)"
    },
    {
        "college_name": "University College of Engineering, Kariavattom (Id: C-44481)",
        "college_type": "Constituent / University College",
        "district": "Thiruvananthapuram",
        "state": "Kerala",
        "university": "Kerala University, Thiruvananthapuram (Id: U-0260)"
    },
    {
        "college_name": "JAWAHARLAL NEHRU MEDICAL COLLEGE (Id: C-24503)",
        "college_type": "Constituent / University College",
        "district": "Belgaum",
        "state": "Karnataka",
        "university": "K.L.E. Academy of Higher Education and Research, Belgaum (Id: U-0225)"
    },
    {
        "college_name": "KLE College of Pharmacy, Bangalore (Id: C-24502)",
        "college_type": "Constituent / University College",
        "district": "Bangalore",
        "state": "Karnataka",
        "university": "K.L.E. Academy of Higher Education and Research, Belgaum (Id: U-0225)"
    },
    {
        "college_name": "KLE COLLEGE OF PHARMACY, BELGAUM (Id: C-24505)",
        "college_type": "Constituent / University College",
        "district": "Belgaum",
        "state": "Karnataka",
        "university": "K.L.E. Academy of Higher Education and Research, Belgaum (Id: U-0225)"
    },
    {
        "college_name": "KLE College of Pharmacy, Hubli (Id: C-24506)",
        "college_type": "Constituent / University College",
        "district": "Dharwad",
        "state": "Karnataka",
        "university": "K.L.E. Academy of Higher Education and Research, Belgaum (Id: U-0225)"
    },
    {
        "college_name": "KLE Institute of Nursing Sciences (Id: C-24500)",
        "college_type": "Constituent / University College",
        "district": "Belgaum",
        "state": "Karnataka",
        "university": "K.L.E. Academy of Higher Education and Research, Belgaum (Id: U-0225)"
    },
    {
        "college_name": "KLE INSTITUTE OF PHYSIOTHERAPY (Id: C-24507)",
        "college_type": "Constituent / University College",
        "district": "Belgaum",
        "state": "Karnataka",
        "university": "K.L.E. Academy of Higher Education and Research, Belgaum (Id: U-0225)"
    },
    {
        "college_name": "KLEU'S SHRI.B.M.K. AYURVEDA MAHAVIDYALAYA,BELGAUM (Id: C-24501)",
        "college_type": "Constituent / University College",
        "district": "Belgaum",
        "state": "Karnataka",
        "university": "K.L.E. Academy of Higher Education and Research, Belgaum (Id: U-0225)"
    },
    {
        "college_name": "KLE VISHWANATH KATTI INSTITUTE OF DENTAL SCIENCES (Id: C-24504)",
        "college_type": "Constituent / University College",
        "district": "Belgaum",
        "state": "Karnataka",
        "university": "K.L.E. Academy of Higher Education and Research, Belgaum (Id: U-0225)"
    },
    {
        "college_name": "ABM college. Jamshedpur (Id: C-44944)",
        "college_type": "Constituent / University College",
        "district": "Purbi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "BAHARAGORA COLLEGE (Id: C-43556)",
        "college_type": "Constituent / University College",
        "district": "Purbi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "G.C. JAIN COMMERCE COLLEGE, CHAIBASA (Id: C-43538)",
        "college_type": "Constituent / University College",
        "district": "Purbi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "GHATSHILA COLLEGE, GHATSILA (Id: C-43541)",
        "college_type": "Constituent / University College",
        "district": "Pashchimi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "JAMSHEDPUR CO-OPERATIVE COLLEGE (Id: C-43559)",
        "college_type": "Constituent / University College",
        "district": "Purbi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "JAMSHEDPUR CO-OPERATIVE LAW COLLEGE, JAMSHEDPUR (Id: C-43553)",
        "college_type": "Constituent / University College",
        "district": "Purbi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "jAMSHEDPUR WORKER'S COLLEGE (Id: C-43544)",
        "college_type": "Constituent / University College",
        "district": "Pashchimi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "jJAMSHEDPUR WOMENS COLLEGE (Id: C-43563)",
        "college_type": "Constituent / University College",
        "district": "Purbi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "J.L.N. COLLEGE ,CHAKRADHARPUR (Id: C-43543)",
        "college_type": "Constituent / University College",
        "district": "Purbi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "J.L.N. COLLEGE, CHAKRADHARPUR (Id: C-43564)",
        "college_type": "Constituent / University College",
        "district": "Pashchimi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "K.S. COLLEGE, SERAIKELLA (Id: C-43540)",
        "college_type": "Constituent / University College",
        "district": "Pashchimi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "L.B.S.M. COLLEGE, JAMSHEDPUR (Id: C-43548)",
        "college_type": "Constituent / University College",
        "district": "Purbi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "MAHILA COLLEGE, CHAIBASA (Id: C-43542)",
        "college_type": "Constituent / University College",
        "district": "Pashchimi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "S.B. COLLEGE, CHANDIL (Id: C-43555)",
        "college_type": "Constituent / University College",
        "district": "Purbi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "TATA COLLEGE, CHAIBASA (Id: C-43549)",
        "college_type": "Constituent / University College",
        "district": "Pashchimi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "THE GRADUATE SCHOOL COLLEGE FOR WOMEN, JAMSHEDPUR (Id: C-43558)",
        "college_type": "Constituent / University College",
        "district": "Purbi Singhbhum",
        "state": "Jharkhand",
        "university": "Kolhan University, West Singhbhum (Id: U-0206)"
    },
    {
        "college_name": "KONERU LAKSHMAIAH COLLEGE OF ENGINEERING (Id: C-33028)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Koneru Lakshmaiah Education Foundation,Guntur (Id: U-0020)"
    },
    {
        "college_name": "Krishna College of Physiotherapy, Karad (Id: C-23035)",
        "college_type": "Constituent / University College",
        "district": "Satara",
        "state": "Maharashtra",
        "university": "Krishna Institute of Medical Sciences Deemed University, Karad (Id: U-0311)"
    },
    {
        "college_name": "Krishna Institute of Biotechnology & Bioinformatics, Karad (Id: C-23037)",
        "college_type": "Constituent / University College",
        "district": "Satara",
        "state": "Maharashtra",
        "university": "Krishna Institute of Medical Sciences Deemed University, Karad (Id: U-0311)"
    },
    {
        "college_name": "Krishna Institute of Medical Sciences, Karad (Id: C-23033)",
        "college_type": "Constituent / University College",
        "district": "Satara",
        "state": "Maharashtra",
        "university": "Krishna Institute of Medical Sciences Deemed University, Karad (Id: U-0311)"
    },
    {
        "college_name": "Krishna Institute of Nursing Sciences, Karad (Id: C-23034)",
        "college_type": "Constituent / University College",
        "district": "Satara",
        "state": "Maharashtra",
        "university": "Krishna Institute of Medical Sciences Deemed University, Karad (Id: U-0311)"
    },
    {
        "college_name": "Krishna School of Dental Sciences, Karad (Id: C-23036)",
        "college_type": "Constituent / University College",
        "district": "Satara",
        "state": "Maharashtra",
        "university": "Krishna Institute of Medical Sciences Deemed University, Karad (Id: U-0311)"
    },
    {
        "college_name": "University College of Education (Id: C-10532)",
        "college_type": "Constituent / University College",
        "district": "Kurukshetra",
        "state": "Haryana",
        "university": "Kurukshetra University, Kurukshetra (Id: U-0164)"
    },
    {
        "college_name": "University UG College (Id: C-10594)",
        "college_type": "Constituent / University College",
        "district": "Kurukshetra",
        "state": "Haryana",
        "university": "Kurukshetra University, Kurukshetra (Id: U-0164)"
    },
    {
        "college_name": "Sahyadri Arts & Commerce College, Shimoga. (Id: C-17823)",
        "college_type": "Constituent / University College",
        "district": "Shimoga",
        "state": "Karnataka",
        "university": "Kuvempu University, Shankaraghatta, Shimoga (Id: U-0232)"
    },
    {
        "college_name": "Sahyadri Science College, Shimoga. (Id: C-17829)",
        "college_type": "Constituent / University College",
        "district": "Shimoga",
        "state": "Karnataka",
        "university": "Kuvempu University, Shankaraghatta, Shimoga (Id: U-0232)"
    },
    {
        "college_name": "S.M.R. Arts & Commerce College, Shankaraghatta. (Id: C-17769)",
        "college_type": "Constituent / University College",
        "district": "Shimoga",
        "state": "Karnataka",
        "university": "Kuvempu University, Shankaraghatta, Shimoga (Id: U-0232)"
    },
    {
        "college_name": "College of Veterinary Sciences (Id: C-35388)",
        "college_type": "Constituent / University College",
        "district": "Hisar",
        "state": "Haryana",
        "university": "Lala lajpat Rai University of Veterinary and Animal Sciences (Id: U-0165)"
    },
    {
        "college_name": "A.N.D. College (Id: C-8787)",
        "college_type": "Constituent / University College",
        "district": "Samastipur",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "A. P.S.M. College (Id: C-8784)",
        "college_type": "Constituent / University College",
        "district": "Begusarai",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "B. M. A. College (Id: C-8767)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "B. M.College,Rahika (Id: C-8759)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "B.R.B. College (Id: C-8752)",
        "college_type": "Constituent / University College",
        "district": "Samastipur",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "C.M.B. College (Id: C-8724)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "C. M. College (Id: C-8712)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "C.M.J. College (Id: C-8713)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "C. M. Law College (Id: C-8718)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "C. M. Sc. College (Id: C-8774)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "D.B. College (Id: C-8727)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "D.B.K.N. College (Id: C-8743)",
        "college_type": "Constituent / University College",
        "district": "Samastipur",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "Dr. L.K.V.D.College (Id: C-8755)",
        "college_type": "Constituent / University College",
        "district": "Samastipur",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "G.D. College (Id: C-8771)",
        "college_type": "Constituent / University College",
        "district": "Begusarai",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "G.M.R.D. College (Id: C-8780)",
        "college_type": "Constituent / University College",
        "district": "Samastipur",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "H.P.S College, Madhepur (Id: C-8732)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "J. K. College, Biraul (Id: C-8764)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "J.M.D.P.L.M. College (Id: C-8761)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "J.N. College (Id: C-8733)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "J. N. College, Nehra (Id: C-8711)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "K. S. College (Id: C-8779)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "K.V.Sc. College, (Id: C-8760)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "L. N.J. College (Id: C-8739)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "Marwari College (Id: C-8754)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "Millat College (Id: C-8722)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "M. K. College (Id: C-8776)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "M.K.S. College (Id: C-8769)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "M. L.S. College (Id: C-8740)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "M.L.S.M. College (Id: C-8768)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "M. R. M. College (Id: C-8736)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "R.B. College (Id: C-8715)",
        "college_type": "Constituent / University College",
        "district": "Samastipur",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "R.B.S. College, Andaur (Id: C-8790)",
        "college_type": "Constituent / University College",
        "district": "Samastipur",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "R.C.S. College (Id: C-8741)",
        "college_type": "Constituent / University College",
        "district": "Begusarai",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "R. K. College (Id: C-8786)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "R.N.A.R. College (Id: C-8763)",
        "college_type": "Constituent / University College",
        "district": "Samastipur",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "R.N.College (Id: C-8714)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "Samastipur College (Id: C-8728)",
        "college_type": "Constituent / University College",
        "district": "Samastipur",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "SBSS College (Id: C-8720)",
        "college_type": "Constituent / University College",
        "district": "Begusarai",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "S.K. Mahila College (Id: C-8757)",
        "college_type": "Constituent / University College",
        "district": "Begusarai",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "U.P. College (Id: C-8744)",
        "college_type": "Constituent / University College",
        "district": "Samastipur",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "U.R. College, Rosera (Id: C-8737)",
        "college_type": "Constituent / University College",
        "district": "Samastipur",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "V.S.J. College (Id: C-8717)",
        "college_type": "Constituent / University College",
        "district": "Madhubani",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "Women's College (Id: C-8777)",
        "college_type": "Constituent / University College",
        "district": "Samastipur",
        "state": "Bihar",
        "university": "Lalit Narayan Mithila University, Darbhanga (Id: U-0068)"
    },
    {
        "college_name": "University Of Madras Constituent College - Nemmili (Id: C-43999)",
        "college_type": "Constituent / University College",
        "district": "Chennai",
        "state": "Tamil Nadu",
        "university": "Madras University, Chennai (Id: U-0462)"
    },
    {
        "college_name": "University Of Madras Constituent College - Thiruvottiyur (Id: C-43961)",
        "college_type": "Constituent / University College",
        "district": "Chennai",
        "state": "Tamil Nadu",
        "university": "Madras University, Chennai (Id: U-0462)"
    },
    {
        "college_name": "MADURAI KAMARAJ UNIVERSITY COLLEGE, AUNDIPATTI (Id: C-36507)",
        "college_type": "Constituent / University College",
        "district": "Theni",
        "state": "Tamil Nadu",
        "university": "Madurai Kamraj University, Madurai (Id: U-0463)"
    },
    {
        "college_name": "MADURAI KAMARAJ UNIVERSITY COLLEGE, SATTUR (Id: C-36525)",
        "college_type": "Constituent / University College",
        "district": "Virudhunagar",
        "state": "Tamil Nadu",
        "university": "Madurai Kamraj University, Madurai (Id: U-0463)"
    },
    {
        "college_name": "MADURAI KAMARAJ UNIVERSITY CONSTITUENT COLLEGE, DINDIGUL (Id: C-45942)",
        "college_type": "Constituent / University College",
        "district": "Dindigul",
        "state": "Tamil Nadu",
        "university": "Madurai Kamraj University, Madurai (Id: U-0463)"
    },
    {
        "college_name": "MADURAI KAMARAJ UNIVERSTIY COLLEGE, KOTTUR (Id: C-36539)",
        "college_type": "Constituent / University College",
        "district": "Theni",
        "state": "Tamil Nadu",
        "university": "Madurai Kamraj University, Madurai (Id: U-0463)"
    },
    {
        "college_name": "A.M.College (Id: C-12867)",
        "college_type": "Constituent / University College",
        "district": "Gaya",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "A.N.College (Id: C-12939)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "A.N.S. College, Barh (Id: C-12883)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "A.N.S. College,Nabinagar (Id: C-12880)",
        "college_type": "Constituent / University College",
        "district": "Aurangabad",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "B.D.College (Id: C-12847)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "B.S.College, Danapur (Id: C-12955)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "College of Commerce (Id: C-12943)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "Daudnagar College, Daudnagar (Id: C-12868)",
        "college_type": "Constituent / University College",
        "district": "Aurangabad",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "Gaya College, Gaya (Id: C-12911)",
        "college_type": "Constituent / University College",
        "district": "Gaya",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "G.B.M.College (Id: C-12930)",
        "college_type": "Constituent / University College",
        "district": "Gaya",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "G.D.M.College, (Id: C-12878)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "G.J.College, Rambagh, Bihta (Id: C-12929)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "J.D. Women's College (Id: C-12897)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "J.J.College (Id: C-12959)",
        "college_type": "Constituent / University College",
        "district": "Gaya",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "J.N.L.College, Khagaul (Id: C-12919)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "Kisan College, Sohsarai (Id: C-12907)",
        "college_type": "Constituent / University College",
        "district": "Nalanda",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "K.L.S.College, (Id: C-12924)",
        "college_type": "Constituent / University College",
        "district": "Nawada",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "K.S.M. College (Id: C-12879)",
        "college_type": "Constituent / University College",
        "district": "Aurangabad",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "Mahila College, Khagaul (Id: C-12854)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "M.D.College, Naubatpur (Id: C-12961)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "M.M.College, Bikram (Id: C-12962)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "Nalanda College, Biharshariff (Id: C-12858)",
        "college_type": "Constituent / University College",
        "district": "Nalanda",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "Nalanda Mahilla College, Biharshariff (Id: C-12850)",
        "college_type": "Constituent / University College",
        "district": "Nalanda",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "R.K.D. College (Id: C-12902)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "R.L.S.Y. College (Id: C-12904)",
        "college_type": "Constituent / University College",
        "district": "Aurangabad",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "R.L.S.Y. College, Bakhtiyarpur (Id: C-12947)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "R.M.W. College (Id: C-12941)",
        "college_type": "Constituent / University College",
        "district": "Nawada",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "R.P.M. College, Patnacity (Id: C-12846)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "R.R.S. College, Mokamah (Id: C-12948)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "S.B.A.N. College, Darheta Lari (Id: C-12861)",
        "college_type": "Constituent / University College",
        "district": "Arwal",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "S.D. College, Kaler (Id: C-12958)",
        "college_type": "Constituent / University College",
        "district": "Jehanabad",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "S.G.G.S. college, Patnacity (Id: C-12917)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "S.M.D. College, Punpun (Id: C-12851)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "S.M.S.G. College, Sherghati (Id: C-12833)",
        "college_type": "Constituent / University College",
        "district": "Gaya",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "S.N.S. College, Tekari (Id: C-12842)",
        "college_type": "Constituent / University College",
        "district": "Gaya",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "S.N.Sinha College, (Id: C-12912)",
        "college_type": "Constituent / University College",
        "district": "Jehanabad",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "S.N.Sinha College, Warsaliganj (Id: C-12932)",
        "college_type": "Constituent / University College",
        "district": "Nawada",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "S.P.M.College, Udantpuri (Id: C-12893)",
        "college_type": "Constituent / University College",
        "district": "Nalanda",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "Sri Arvind Mahila College (Id: C-12857)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "S.S.College, (Id: C-12881)",
        "college_type": "Constituent / University College",
        "district": "Jehanabad",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "S.Sinha College (Id: C-12882)",
        "college_type": "Constituent / University College",
        "district": "Aurangabad",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "S.U.College,Hilsa (Id: C-12837)",
        "college_type": "Constituent / University College",
        "district": "Nalanda",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "T.P.s. College, (Id: C-12925)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "T.S. College, Hisua (Id: C-12899)",
        "college_type": "Constituent / University College",
        "district": "Nawada",
        "state": "Bihar",
        "university": "Magadh University, Bodh Gaya (Id: U-0069)"
    },
    {
        "college_name": "M.J. College of Commerce (Id: C-7194)",
        "college_type": "Constituent / University College",
        "district": "Bhavnagar",
        "state": "Gujarat",
        "university": "Maharaja Krishnakumarsinhji Bhavnagar University (Id: U-0124)"
    },
    {
        "college_name": "Samaldas Arts College (Id: C-7187)",
        "college_type": "Constituent / University College",
        "district": "Bhavnagar",
        "state": "Gujarat",
        "university": "Maharaja Krishnakumarsinhji Bhavnagar University (Id: U-0124)"
    },
    {
        "college_name": "Sir P.P. Institute of Science (Id: C-7203)",
        "college_type": "Constituent / University College",
        "district": "Bhavnagar",
        "state": "Gujarat",
        "university": "Maharaja Krishnakumarsinhji Bhavnagar University (Id: U-0124)"
    },
    {
        "college_name": "Baroda Sanskrit Mahavidhyalay (Id: C-7225)",
        "college_type": "Constituent / University College",
        "district": "Vadodara",
        "state": "Gujarat",
        "university": "Maharaja Sayajirao University of Baroda, Vadodara (Id: U-0143)"
    },
    {
        "college_name": "M K Amin Arts and Science & College of Commerce (Id: C-7224)",
        "college_type": "Constituent / University College",
        "district": "Vadodara",
        "state": "Gujarat",
        "university": "Maharaja Sayajirao University of Baroda, Vadodara (Id: U-0143)"
    },
    {
        "college_name": "Polytechnic College (Id: C-7223)",
        "college_type": "Constituent / University College",
        "district": "Vadodara",
        "state": "Gujarat",
        "university": "Maharaja Sayajirao University of Baroda, Vadodara (Id: U-0143)"
    },
    {
        "college_name": "Bombay Veterinary College, Mumbai (Id: C-44021)",
        "college_type": "Constituent / University College",
        "district": "Mumbai",
        "state": "Maharashtra",
        "university": "Maharashtra Animal & Fishery Sciences University, Nagpur (Id: U-0312)"
    },
    {
        "college_name": "College of Dairy Technology, Udgir (Id: C-44025)",
        "college_type": "Constituent / University College",
        "district": "Latur",
        "state": "Maharashtra",
        "university": "Maharashtra Animal & Fishery Sciences University, Nagpur (Id: U-0312)"
    },
    {
        "college_name": "College of Dairy Technology, Warud (Pusad) (Id: C-44020)",
        "college_type": "Constituent / University College",
        "district": "Yavatmal",
        "state": "Maharashtra",
        "university": "Maharashtra Animal & Fishery Sciences University, Nagpur (Id: U-0312)"
    },
    {
        "college_name": "College of Fishery Sciences, Nagpur (Id: C-44019)",
        "college_type": "Constituent / University College",
        "district": "Nagpur",
        "state": "Maharashtra",
        "university": "Maharashtra Animal & Fishery Sciences University, Nagpur (Id: U-0312)"
    },
    {
        "college_name": "College of Fishery Sciences, Udgir (Id: C-44026)",
        "college_type": "Constituent / University College",
        "district": "Latur",
        "state": "Maharashtra",
        "university": "Maharashtra Animal & Fishery Sciences University, Nagpur (Id: U-0312)"
    },
    {
        "college_name": "College of Veterinary & Animal Sciences, Parbhani (Id: C-44027)",
        "college_type": "Constituent / University College",
        "district": "Parbhani",
        "state": "Maharashtra",
        "university": "Maharashtra Animal & Fishery Sciences University, Nagpur (Id: U-0312)"
    },
    {
        "college_name": "College of Veterinary & Animal Sciences, Udgir (Id: C-44022)",
        "college_type": "Constituent / University College",
        "district": "Latur",
        "state": "Maharashtra",
        "university": "Maharashtra Animal & Fishery Sciences University, Nagpur (Id: U-0312)"
    },
    {
        "college_name": "Krantisinh Nana Patil College of Veterinary Science, Shirwal (Id: C-44024)",
        "college_type": "Constituent / University College",
        "district": "Satara",
        "state": "Maharashtra",
        "university": "Maharashtra Animal & Fishery Sciences University, Nagpur (Id: U-0312)"
    },
    {
        "college_name": "Nagpur Veterinary College, Nagpur (Id: C-44018)",
        "college_type": "Constituent / University College",
        "district": "Nagpur",
        "state": "Maharashtra",
        "university": "Maharashtra Animal & Fishery Sciences University, Nagpur (Id: U-0312)"
    },
    {
        "college_name": "Post Graduate Institute of Veterinary & Animal Sciences (Id: C-44023)",
        "college_type": "Constituent / University College",
        "district": "Akola",
        "state": "Maharashtra",
        "university": "Maharashtra Animal & Fishery Sciences University, Nagpur (Id: U-0312)"
    },
    {
        "college_name": "Dept. of Law, MM University, Mullana-Ambala. (Id: C-7040)",
        "college_type": "Constituent / University College",
        "district": "Ambala",
        "state": "Haryana",
        "university": "Maharishi Markandeshwar University, Mullana-Ambala (Id: U-0168)"
    },
    {
        "college_name": "MM College of Dental Sciences & Research, Mullana-Ambala. (Id: C-7043)",
        "college_type": "Constituent / University College",
        "district": "Ambala",
        "state": "Haryana",
        "university": "Maharishi Markandeshwar University, Mullana-Ambala (Id: U-0168)"
    },
    {
        "college_name": "MM College of Nursing, Mullana-Ambala. (Id: C-7047)",
        "college_type": "Constituent / University College",
        "district": "Ambala",
        "state": "Haryana",
        "university": "Maharishi Markandeshwar University, Mullana-Ambala (Id: U-0168)"
    },
    {
        "college_name": "MM College of Pharmacy, Mullana-Ambala. (Id: C-7041)",
        "college_type": "Constituent / University College",
        "district": "Ambala",
        "state": "Haryana",
        "university": "Maharishi Markandeshwar University, Mullana-Ambala (Id: U-0168)"
    },
    {
        "college_name": "MM Engg. College, Mullana-Ambala (Id: C-7045)",
        "college_type": "Constituent / University College",
        "district": "Ambala",
        "state": "Haryana",
        "university": "Maharishi Markandeshwar University, Mullana-Ambala (Id: U-0168)"
    },
    {
        "college_name": "MM Institute of Computer Technology & Business Mgt. (Hotel Mgt.), Mullana-Ambala. (Id: C-7042)",
        "college_type": "Constituent / University College",
        "district": "Ambala",
        "state": "Haryana",
        "university": "Maharishi Markandeshwar University, Mullana-Ambala (Id: U-0168)"
    },
    {
        "college_name": "MM Institute of Computer Technology & Business Mgt. (MCA), Mullana-Ambala (Id: C-7044)",
        "college_type": "Constituent / University College",
        "district": "Ambala",
        "state": "Haryana",
        "university": "Maharishi Markandeshwar University, Mullana-Ambala (Id: U-0168)"
    },
    {
        "college_name": "MM Institute of Management, Mullana-Ambala. (Id: C-7037)",
        "college_type": "Constituent / University College",
        "district": "Ambala",
        "state": "Haryana",
        "university": "Maharishi Markandeshwar University, Mullana-Ambala (Id: U-0168)"
    },
    {
        "college_name": "MM Institute of Medical Sciences & Research, Mullana-Ambala. (Id: C-7046)",
        "college_type": "Constituent / University College",
        "district": "Ambala",
        "state": "Haryana",
        "university": "Maharishi Markandeshwar University, Mullana-Ambala (Id: U-0168)"
    },
    {
        "college_name": "MM Institute of Nursing (for girls only), Mullana-Ambala. (Id: C-7038)",
        "college_type": "Constituent / University College",
        "district": "Ambala",
        "state": "Haryana",
        "university": "Maharishi Markandeshwar University, Mullana-Ambala (Id: U-0168)"
    },
    {
        "college_name": "MM Institute of Physiotherapy & Rehabilitation, Mullana-Ambala. (Id: C-7039)",
        "college_type": "Constituent / University College",
        "district": "Ambala",
        "state": "Haryana",
        "university": "Maharishi Markandeshwar University, Mullana-Ambala (Id: U-0168)"
    },
    {
        "college_name": "ILMS, Gurgaon (Id: C-28359)",
        "college_type": "Constituent / University College",
        "district": "Gurgaon",
        "state": "Haryana",
        "university": "Maharshi Dayanand University, Rohtak (Id: U-0167)"
    },
    {
        "college_name": "University College of Applied Life Sciences, Chuttippara, Pathanamthitta (Id: C-11719)",
        "college_type": "Constituent / University College",
        "district": "Pathanamthitta",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Applied Sciences, Chuttippara, Pathanamthitta (Id: C-11738)",
        "college_type": "Constituent / University College",
        "district": "Pathanamthitta",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Applied Sciences, Edappally, Kochi, Ernakulam (Id: C-11800)",
        "college_type": "Constituent / University College",
        "district": "Ernakulam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Applied Sciences, Pullarikunnu, Malloossery, Kottayam (Id: C-11750)",
        "college_type": "Constituent / University College",
        "district": "Kottayam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Engineering, Muttom, Thodupuzha, Idukki (Id: C-11606)",
        "college_type": "Constituent / University College",
        "district": "Idukki",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Medical Education, Main Centre, Arpookara, Gandhinagar P.O., Kottayam (Id: C-11768)",
        "college_type": "Constituent / University College",
        "district": "Kottayam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Medical Education, Manimalakunnu, Ernakulam Dist. (Id: C-11805)",
        "college_type": "Constituent / University College",
        "district": "Ernakulam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Medical Education, Regional Centre, Municipal Building, Railway Station Road, Angamaly, Ernakulam (Id: C-11692)",
        "college_type": "Constituent / University College",
        "district": "Ernakulam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Medical Education, Regional centre, Our Towers, TD Road, Ernakulam (Id: C-11707)",
        "college_type": "Constituent / University College",
        "district": "Ernakulam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Medical Education, Regional Centre, PKV Buildings, Perumanoor P.O., Thevara, Ernakulam (Id: C-11617)",
        "college_type": "Constituent / University College",
        "district": "Ernakulam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Medical Education, RIMSR, Rubber Board P.O., Thalappady, Kottayam (Id: C-11737)",
        "college_type": "Constituent / University College",
        "district": "Kottayam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Nursing, Andoor, Marangattupally P.O., Pala, Kottayam (Id: C-11714)",
        "college_type": "Constituent / University College",
        "district": "Kottayam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Nursing, Angamaly, Ernakulam (Id: C-11628)",
        "college_type": "Constituent / University College",
        "district": "Ernakulam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Nursing, Chuttippara, Pathanamthitta (Id: C-11718)",
        "college_type": "Constituent / University College",
        "district": "Pathanamthitta",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Nursing, Gandhinagar, Kottayam (Id: C-11674)",
        "college_type": "Constituent / University College",
        "district": "Kottayam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Nursing, Manimalakkunnu, Ernakulam (Id: C-11725)",
        "college_type": "Constituent / University College",
        "district": "Ernakulam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Nursing, Nedumkandam, Idukki (Id: C-11795)",
        "college_type": "Constituent / University College",
        "district": "Idukki",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Nursing, T.D. Road, Ernakulam (Id: C-11642)",
        "college_type": "Constituent / University College",
        "district": "Ernakulam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Nursing, Thalappady, Kottayam (Id: C-11836)",
        "college_type": "Constituent / University College",
        "district": "Kottayam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Nursing, Thevara, Ernakulam (Id: C-11700)",
        "college_type": "Constituent / University College",
        "district": "Ernakulam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Pharmacy, Cheruvandoor, Ettumanoor P.O., Kottayam (Id: C-11743)",
        "college_type": "Constituent / University College",
        "district": "Kottayam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Pharmacy, Thalappady, Kottayam (Id: C-11759)",
        "college_type": "Constituent / University College",
        "district": "Kottayam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Teacher Education, Amaravathy P.O., Kumily 685 509, Idukki (Id: C-11741)",
        "college_type": "Constituent / University College",
        "district": "Idukki",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Teacher Education, Government Girls High School Campus, Vaikom, Kottayam (Id: C-11590)",
        "college_type": "Constituent / University College",
        "district": "Kottayam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Teacher Education, Government Higher Secondary School, Thekkekara, Erattupetta, Kottayam (Id: C-11686)",
        "college_type": "Constituent / University College",
        "district": "Kottayam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Teacher Education, Government High School Campus, Kudamaloor, Kottayam (Id: C-11699)",
        "college_type": "Constituent / University College",
        "district": "Kottayam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Teacher Education, Government High School Campus, Paippad, Changanacherry, Kottayam (Id: C-11818)",
        "college_type": "Constituent / University College",
        "district": "Kottayam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Teacher Education, Government High School Campus, Petta, Kanjirappally, Kottayam (Id: C-11677)",
        "college_type": "Constituent / University College",
        "district": "Kottayam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Teacher Education, Government High School Campus, Thodupuzha, Idukki (Id: C-11766)",
        "college_type": "Constituent / University College",
        "district": "Idukki",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Teacher Education, Government Model High School Campus, Muvattupuzha, Ernakulam (Id: C-11782)",
        "college_type": "Constituent / University College",
        "district": "Ernakulam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Teacher Education, Near Government Boys High School Campus, Vaikom Road, Thrippunithura, Ernakulam (Id: C-11662)",
        "college_type": "Constituent / University College",
        "district": "Ernakulam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Teacher Education, Panchayat U.P. School Campus, Nedumkandam, Idukki (Id: C-11675)",
        "college_type": "Constituent / University College",
        "district": "Idukki",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Teacher Education, Thottakkad P.O., Kottayam (Id: C-11626)",
        "college_type": "Constituent / University College",
        "district": "Kottayam",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "University College of Teacher Education, Vocational Higher Secondary School Campus, Elanthoor, Pathanamthitta (Id: C-11791)",
        "college_type": "Constituent / University College",
        "district": "Pathanamthitta",
        "state": "Kerala",
        "university": "Mahatma Gandhi University, Kottayam (Id: U-0262)"
    },
    {
        "college_name": "MAHATMA GANDHI DENTAL COLLEGE AND HOSPITAL, JAIPUR (Id: C-49501)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "MAHATMA GANDHI UNIVERSITY OF MEDICAL SCIENCES AND TECHNOLOGY, JAIPUR (Id: U-0732)"
    },
    {
        "college_name": "MAHATMA GANDHI MEDICAL COLLEGE AND HOSPITAL, JAIPUR (Id: C-49500)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "MAHATMA GANDHI UNIVERSITY OF MEDICAL SCIENCES AND TECHNOLOGY, JAIPUR (Id: U-0732)"
    },
    {
        "college_name": "MAHATMA GANDHI NURSING COLLEGE, JAIPUR (Id: C-49502)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "MAHATMA GANDHI UNIVERSITY OF MEDICAL SCIENCES AND TECHNOLOGY, JAIPUR (Id: U-0732)"
    },
    {
        "college_name": "MAHATMA GANDHI NURSING SCHOOL, JAIPUR (Id: C-49504)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "MAHATMA GANDHI UNIVERSITY OF MEDICAL SCIENCES AND TECHNOLOGY, JAIPUR (Id: U-0732)"
    },
    {
        "college_name": "MAHATMA GANDHI PHYSIOTHERAPY COLLEGE, JAIPUR (Id: C-49503)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "MAHATMA GANDHI UNIVERSITY OF MEDICAL SCIENCES AND TECHNOLOGY, JAIPUR (Id: U-0732)"
    },
    {
        "college_name": "College of Agriculture, Dhule (Id: C-44573)",
        "college_type": "Constituent / University College",
        "district": "Dhule",
        "state": "Maharashtra",
        "university": "Mahatma Phule Krishi Vidyapeeth, Rahuri (Id: U-0315)"
    },
    {
        "college_name": "College of Agriculture, Kolhapur (Id: C-44569)",
        "college_type": "Constituent / University College",
        "district": "Kolhapur",
        "state": "Maharashtra",
        "university": "Mahatma Phule Krishi Vidyapeeth, Rahuri (Id: U-0315)"
    },
    {
        "college_name": "College Of Agriculture, Shivajinagar, Pune (Id: C-44571)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Mahatma Phule Krishi Vidyapeeth, Rahuri (Id: U-0315)"
    },
    {
        "college_name": "Dr. Annasaheb Shinde College of Agriculture Eng., Rahuri (Id: C-44572)",
        "college_type": "Constituent / University College",
        "district": "Ahmadnagar",
        "state": "Maharashtra",
        "university": "Mahatma Phule Krishi Vidyapeeth, Rahuri (Id: U-0315)"
    },
    {
        "college_name": "Post Graduate Institute, Rahuri (Id: C-44570)",
        "college_type": "Constituent / University College",
        "district": "Ahmadnagar",
        "state": "Maharashtra",
        "university": "Mahatma Phule Krishi Vidyapeeth, Rahuri (Id: U-0315)"
    },
    {
        "college_name": "Field Marshal K.M. Cariappa College, Madikeri (Id: C-16864)",
        "college_type": "Constituent / University College",
        "district": "Kodagu",
        "state": "Karnataka",
        "university": "Mangalore University, Mangalore (Id: U-0233)"
    },
    {
        "college_name": "University College, Mangalore (Id: C-16872)",
        "college_type": "Constituent / University College",
        "district": "Dakshina Kannada",
        "state": "Karnataka",
        "university": "Mangalore University, Mangalore (Id: U-0233)"
    },
    {
        "college_name": "Kasturba Medical College, Mangalore (Id: C-7251)",
        "college_type": "Constituent / University College",
        "district": "Dakshina Kannada",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Kasturba Medical College, Manipal (Id: C-7242)",
        "college_type": "Constituent / University College",
        "district": "Udupi",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Manipal Centre for Information Sciences, Manipal (Id: C-7241)",
        "college_type": "Constituent / University College",
        "district": "Udupi",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Manipal College of Allied Health Sciences, Manipal (Id: C-7255)",
        "college_type": "Constituent / University College",
        "district": "Udupi",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Manipal College of Dental Sciences, Mangalore (Id: C-7240)",
        "college_type": "Constituent / University College",
        "district": "Dakshina Kannada",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Manipal College of Dental Sciences, Manipal (Id: C-7254)",
        "college_type": "Constituent / University College",
        "district": "Udupi",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Manipal College of Nursing Bangalore (Id: C-7250)",
        "college_type": "Constituent / University College",
        "district": "Bangalore",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Manipal College of Nursing, Mangalore (Id: C-7243)",
        "college_type": "Constituent / University College",
        "district": "Dakshina Kannada",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Manipal College of Nursing, Manipal (Id: C-7247)",
        "college_type": "Constituent / University College",
        "district": "Udupi",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Manipal College of Pharmaceutical Sciences, Manipal (Id: C-7249)",
        "college_type": "Constituent / University College",
        "district": "Udupi",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Manipal Institute of Communication, Manipal (Id: C-7245)",
        "college_type": "Constituent / University College",
        "district": "Udupi",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Manipal Institute of Jewellary Management, Manipal (Id: C-7239)",
        "college_type": "Constituent / University College",
        "district": "Udupi",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Manipal Institute of Management, Manipal (Id: C-7244)",
        "college_type": "Constituent / University College",
        "district": "Udupi",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Manipal Institute of Regenerative Medicine, Bangalore (Id: C-7253)",
        "college_type": "Constituent / University College",
        "district": "Bangalore",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Manipal Institute of Technology, Manipal (Id: C-7252)",
        "college_type": "Constituent / University College",
        "district": "Udupi",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Manipal Life Science Centre, Manipal (Id: C-7248)",
        "college_type": "Constituent / University College",
        "district": "Udupi",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "MANIPAL SCHOOL OF ARCHITECTURE AND PLANNING, MANIPAL (Id: C-46330)",
        "college_type": "Constituent / University College",
        "district": "Udupi",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "MELAKA MANIPAL MEDICAL COLLEGE, MANIPAL (Id: C-46331)",
        "college_type": "Constituent / University College",
        "district": "Udupi",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Welcomgroup Graduate School of Hotel Administration, Manipal (Id: C-7246)",
        "college_type": "Constituent / University College",
        "district": "Udupi",
        "state": "Karnataka",
        "university": "Manipal Academy of Higher Education, Manipal (Id: U-0234)"
    },
    {
        "college_name": "Manipur Institute of Technology (Id: C-9388)",
        "college_type": "Constituent / University College",
        "district": "Imphal West",
        "state": "Manipur",
        "university": "Manipur University, Imphal (Id: U-0337)"
    },
    {
        "college_name": "Manonmaniam Sundaranar University College, Govindaperi. (Id: C-41194)",
        "college_type": "Constituent / University College",
        "district": "Tirunelveli",
        "state": "Tamil Nadu",
        "university": "Manonmaniam Sundaranar University, Tirunelveli (Id: U-0464)"
    },
    {
        "college_name": "Manonmaniam Sundaranar University College, Nagampatti, (Id: C-41196)",
        "college_type": "Constituent / University College",
        "district": "Thoothukkudi",
        "state": "Tamil Nadu",
        "university": "Manonmaniam Sundaranar University, Tirunelveli (Id: U-0464)"
    },
    {
        "college_name": "Manonmaniam Sundaranar University College, Panakudi (Id: C-41188)",
        "college_type": "Constituent / University College",
        "district": "Tirunelveli",
        "state": "Tamil Nadu",
        "university": "Manonmaniam Sundaranar University, Tirunelveli (Id: U-0464)"
    },
    {
        "college_name": "Manonmaniam Sundaranar University College, Puliankudi (Id: C-41181)",
        "college_type": "Constituent / University College",
        "district": "Tirunelveli",
        "state": "Tamil Nadu",
        "university": "Manonmaniam Sundaranar University, Tirunelveli (Id: U-0464)"
    },
    {
        "college_name": "Manonmaniam Sundaranar University College, Sankarankovil (Id: C-41182)",
        "college_type": "Constituent / University College",
        "district": "Tirunelveli",
        "state": "Tamil Nadu",
        "university": "Manonmaniam Sundaranar University, Tirunelveli (Id: U-0464)"
    },
    {
        "college_name": "Manonmaniam Sundaranar University College, Thisayanvillai (Id: C-41192)",
        "college_type": "Constituent / University College",
        "district": "Tirunelveli",
        "state": "Tamil Nadu",
        "university": "Manonmaniam Sundaranar University, Tirunelveli (Id: U-0464)"
    },
    {
        "college_name": "MANONMANIAM SUNDARANAR UNIVERSITY CONSTITUENT COLLEGE, KADAYANALLUR (Id: C-48311)",
        "college_type": "Constituent / University College",
        "district": "Tirunelveli",
        "state": "Tamil Nadu",
        "university": "Manonmaniam Sundaranar University, Tirunelveli (Id: U-0464)"
    },
    {
        "college_name": "MANONMANIAM SUNDARANAR UNIVERSITY CONSTITUENT COLLEGE, KANYAKUMARI (Id: C-48312)",
        "college_type": "Constituent / University College",
        "district": "Kanniyakumari",
        "state": "Tamil Nadu",
        "university": "Manonmaniam Sundaranar University, Tirunelveli (Id: U-0464)"
    },
    {
        "college_name": "Manonmaniam Sundaranar University Constituent College, Nagalapuram, (Id: C-41162)",
        "college_type": "Constituent / University College",
        "district": "Thoothukkudi",
        "state": "Tamil Nadu",
        "university": "Manonmaniam Sundaranar University, Tirunelveli (Id: U-0464)"
    },
    {
        "college_name": "Manonmaniam Sundaranar University Constituent College, Sattankulam- 628 704, Thoothukudi Dist. (Id: C-41179)",
        "college_type": "Constituent / University College",
        "district": "Thoothukkudi",
        "state": "Tamil Nadu",
        "university": "Manonmaniam Sundaranar University, Tirunelveli (Id: U-0464)"
    },
    {
        "college_name": "College of Agricultural Biotechnology, Latur (Id: C-44511)",
        "college_type": "Constituent / University College",
        "district": "Latur",
        "state": "Maharashtra",
        "university": "Marathwada Agricultural University, Parbhani (Id: U-0316)"
    },
    {
        "college_name": "College of Agricultural Engineering, Parbhani (Id: C-44501)",
        "college_type": "Constituent / University College",
        "district": "Parbhani",
        "state": "Maharashtra",
        "university": "Marathwada Agricultural University, Parbhani (Id: U-0316)"
    },
    {
        "college_name": "College of Agriculture, Ambajogai (Id: C-44495)",
        "college_type": "Constituent / University College",
        "district": "Bid",
        "state": "Maharashtra",
        "university": "Marathwada Agricultural University, Parbhani (Id: U-0316)"
    },
    {
        "college_name": "College of Agriculture, Badnapur (Id: C-44531)",
        "college_type": "Constituent / University College",
        "district": "Jalna",
        "state": "Maharashtra",
        "university": "Marathwada Agricultural University, Parbhani (Id: U-0316)"
    },
    {
        "college_name": "College of Agriculture, Latur (Id: C-44496)",
        "college_type": "Constituent / University College",
        "district": "Latur",
        "state": "Maharashtra",
        "university": "Marathwada Agricultural University, Parbhani (Id: U-0316)"
    },
    {
        "college_name": "College of Agriculture, Parbhani (Id: C-44523)",
        "college_type": "Constituent / University College",
        "district": "Parbhani",
        "state": "Maharashtra",
        "university": "Marathwada Agricultural University, Parbhani (Id: U-0316)"
    },
    {
        "college_name": "College of Food Technology, Parbhani (Id: C-44492)",
        "college_type": "Constituent / University College",
        "district": "Parbhani",
        "state": "Maharashtra",
        "university": "Marathwada Agricultural University, Parbhani (Id: U-0316)"
    },
    {
        "college_name": "College of Home Science, Parbhani (Id: C-44524)",
        "college_type": "Constituent / University College",
        "district": "Parbhani",
        "state": "Maharashtra",
        "university": "Marathwada Agricultural University, Parbhani (Id: U-0316)"
    },
    {
        "college_name": "College of Horticulture, Parbhani (Id: C-44514)",
        "college_type": "Constituent / University College",
        "district": "Parbhani",
        "state": "Maharashtra",
        "university": "Marathwada Agricultural University, Parbhani (Id: U-0316)"
    },
    {
        "college_name": "College og Agriculture, Osmanabd (Id: C-44500)",
        "college_type": "Constituent / University College",
        "district": "Osmanabad",
        "state": "Maharashtra",
        "university": "Marathwada Agricultural University, Parbhani (Id: U-0316)"
    },
    {
        "college_name": "Postgraduate Institute For Agriculture Business Management, Chakur (Id: C-44513)",
        "college_type": "Constituent / University College",
        "district": "Latur",
        "state": "Maharashtra",
        "university": "Marathwada Agricultural University, Parbhani (Id: U-0316)"
    },
    {
        "college_name": "College of Teacher Education, Bhopal (Id: C-30808)",
        "college_type": "Constituent / University College",
        "district": "Bhopal",
        "state": "Madhya Pradesh",
        "university": "Maulana Azad National Urdu University, Hyderabad (Id: U-0023)"
    },
    {
        "college_name": "College of Teacher Education, Darbhanga (Id: C-30811)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Maulana Azad National Urdu University, Hyderabad (Id: U-0023)"
    },
    {
        "college_name": "College of Teacher Education, Srinagar (Id: C-30810)",
        "college_type": "Constituent / University College",
        "district": "Srinagar",
        "state": "Jammu and Kashmir",
        "university": "Maulana Azad National Urdu University, Hyderabad (Id: U-0023)"
    },
    {
        "college_name": "MANUU POLYTECHNIC, DARBHANGA (Id: C-46612)",
        "college_type": "Constituent / University College",
        "district": "Darbhanga",
        "state": "Bihar",
        "university": "Maulana Azad National Urdu University, Hyderabad (Id: U-0023)"
    },
    {
        "college_name": "Meenakshi Ammal Dental College, Maduravoyal, Chennai (Id: C-36316)",
        "college_type": "Constituent / University College",
        "district": "Chennai",
        "state": "Tamil Nadu",
        "university": "Meenakshri Academy of Higher Education and Research, Chennai (Id: U-0465)"
    },
    {
        "college_name": "Meenakshi College of Nursing, Mangadu, Chennai (Id: C-36319)",
        "college_type": "Constituent / University College",
        "district": "Kancheepuram",
        "state": "Tamil Nadu",
        "university": "Meenakshri Academy of Higher Education and Research, Chennai (Id: U-0465)"
    },
    {
        "college_name": "Meenakshi College of Physiotherapy, Chennai (Id: C-36317)",
        "college_type": "Constituent / University College",
        "district": "Chennai",
        "state": "Tamil Nadu",
        "university": "Meenakshri Academy of Higher Education and Research, Chennai (Id: U-0465)"
    },
    {
        "college_name": "Meenakshi Medical College and Research Institute, Enathurm Kanchipuram (Id: C-36318)",
        "college_type": "Constituent / University College",
        "district": "Kancheepuram",
        "state": "Tamil Nadu",
        "university": "Meenakshri Academy of Higher Education and Research, Chennai (Id: U-0465)"
    },
    {
        "college_name": "Mahatma Gandhi Mission's College of Nursing, Aurangabad (Id: C-44883)",
        "college_type": "Constituent / University College",
        "district": "Aurangabad",
        "state": "Maharashtra",
        "university": "MGM Institute of Health Sciences, Navi Mumbai (Id: U-0317)"
    },
    {
        "college_name": "Mahatma Gandhi Mission's College of Nursing, Navi Mumbai (Id: C-44876)",
        "college_type": "Constituent / University College",
        "district": "Raigarh",
        "state": "Maharashtra",
        "university": "MGM Institute of Health Sciences, Navi Mumbai (Id: U-0317)"
    },
    {
        "college_name": "Mahatma Gandhi Mission's Medical College,Aurangabad (Id: C-44885)",
        "college_type": "Constituent / University College",
        "district": "Aurangabad",
        "state": "Maharashtra",
        "university": "MGM Institute of Health Sciences, Navi Mumbai (Id: U-0317)"
    },
    {
        "college_name": "Mahatma Gandhi Mission's Medical College,Navi Mumbai (Id: C-44884)",
        "college_type": "Constituent / University College",
        "district": "Raigarh",
        "state": "Maharashtra",
        "university": "MGM Institute of Health Sciences, Navi Mumbai (Id: U-0317)"
    },
    {
        "college_name": "Mahatma Gandhi Mission's New Bombay College of Nursing, Navi Mumbai (Id: C-44882)",
        "college_type": "Constituent / University College",
        "district": "Raigarh",
        "state": "Maharashtra",
        "university": "MGM Institute of Health Sciences, Navi Mumbai (Id: U-0317)"
    },
    {
        "college_name": "Mahatma Gandhi Mission's School of Biomedical Sciences, Aurangabad (Id: C-44881)",
        "college_type": "Constituent / University College",
        "district": "Aurangabad",
        "state": "Maharashtra",
        "university": "MGM Institute of Health Sciences, Navi Mumbai (Id: U-0317)"
    },
    {
        "college_name": "Mahatma Gandhi Mission's School of Biomedical Sciences, Navi Mumbai (Id: C-44878)",
        "college_type": "Constituent / University College",
        "district": "Raigarh",
        "state": "Maharashtra",
        "university": "MGM Institute of Health Sciences, Navi Mumbai (Id: U-0317)"
    },
    {
        "college_name": "Mahatma Gandhi Mission's School of Health Management Studies, Navi Mumbai (Id: C-44879)",
        "college_type": "Constituent / University College",
        "district": "Raigarh",
        "state": "Maharashtra",
        "university": "MGM Institute of Health Sciences, Navi Mumbai (Id: U-0317)"
    },
    {
        "college_name": "Mahatma Gandhi Mission's School of Physiotherapy, Aurangabad (Id: C-44877)",
        "college_type": "Constituent / University College",
        "district": "Aurangabad",
        "state": "Maharashtra",
        "university": "MGM Institute of Health Sciences, Navi Mumbai (Id: U-0317)"
    },
    {
        "college_name": "Mahatma Gandhi Mission's School of Physiotherapy, Navi Mumbai (Id: C-44880)",
        "college_type": "Constituent / University College",
        "district": "Raigarh",
        "state": "Maharashtra",
        "university": "MGM Institute of Health Sciences, Navi Mumbai (Id: U-0317)"
    },
    {
        "college_name": "Dr. M.G.R. Engineering and College (Id: C-36462)",
        "college_type": "Constituent / University College",
        "district": "Thiruvallur",
        "state": "Tamil Nadu",
        "university": "M.G.R. Educational and Research Institute, Chennai (Id: U-0461)"
    },
    {
        "college_name": "Thai Moogambigai Dental College and Hospital (Id: C-36463)",
        "college_type": "Constituent / University College",
        "district": "Thiruvallur",
        "state": "Tamil Nadu",
        "university": "M.G.R. Educational and Research Institute, Chennai (Id: U-0461)"
    },
    {
        "college_name": "Pachhunga University College (Id: C-8308)",
        "college_type": "Constituent / University College",
        "district": "Aizawl",
        "state": "Mizoram",
        "university": "Mizoram University, Aizwal (Id: U-0345)"
    },
    {
        "college_name": "Faculty of Management Studies (Id: C-39918)",
        "college_type": "Constituent / University College",
        "district": "Udaipur",
        "state": "Rajasthan",
        "university": "Mohan Lal Sukhadia University, Uaipur (Id: U-0413)"
    },
    {
        "college_name": "University College of Commerce & Management Studies (Id: C-39882)",
        "college_type": "Constituent / University College",
        "district": "Udaipur",
        "state": "Rajasthan",
        "university": "Mohan Lal Sukhadia University, Uaipur (Id: U-0413)"
    },
    {
        "college_name": "University College of Law (Id: C-39962)",
        "college_type": "Constituent / University College",
        "district": "Udaipur",
        "state": "Rajasthan",
        "university": "Mohan Lal Sukhadia University, Uaipur (Id: U-0413)"
    },
    {
        "college_name": "University College of Science (Id: C-40036)",
        "college_type": "Constituent / University College",
        "district": "Udaipur",
        "state": "Rajasthan",
        "university": "Mohan Lal Sukhadia University, Uaipur (Id: U-0413)"
    },
    {
        "college_name": "University College of Social Science and Humanities (Id: C-39935)",
        "college_type": "Constituent / University College",
        "district": "Udaipur",
        "state": "Rajasthan",
        "university": "Mohan Lal Sukhadia University, Uaipur (Id: U-0413)"
    },
    {
        "college_name": "Mother Teresa Women's University College,Kodaikanal (Id: C-17056)",
        "college_type": "Constituent / University College",
        "district": "Dindigul",
        "state": "Tamil Nadu",
        "university": "Mother Teresa Women's University, Kodaikanal (Id: U-0466)"
    },
    {
        "college_name": "Women's University College of Education,Kodaikanal (Id: C-26531)",
        "college_type": "Constituent / University College",
        "district": "Dindigul",
        "state": "Tamil Nadu",
        "university": "Mother Teresa Women's University, Kodaikanal (Id: U-0466)"
    },
    {
        "college_name": "Sir J. J. College of Architechture (Id: C-33956)",
        "college_type": "Constituent / University College",
        "district": "Mumbai",
        "state": "Maharashtra",
        "university": "Mumbai University Mumbai (Id: U-0318)"
    },
    {
        "college_name": "Maharajas college Mysore (Id: C-17600)",
        "college_type": "Constituent / University College",
        "district": "Mysore",
        "state": "Karnataka",
        "university": "Mysore University, Mysore (Id: U-0235)"
    },
    {
        "college_name": "Maharajas Evening College Mysore (Id: C-17438)",
        "college_type": "Constituent / University College",
        "district": "Mysore",
        "state": "Karnataka",
        "university": "Mysore University, Mysore (Id: U-0235)"
    },
    {
        "college_name": "University college of Fine Arts for Women, Mysore (Id: C-17546)",
        "college_type": "Constituent / University College",
        "district": "Mysore",
        "state": "Karnataka",
        "university": "Mysore University, Mysore (Id: U-0235)"
    },
    {
        "college_name": "Yuvarajas College Mysore (Id: C-17412)",
        "college_type": "Constituent / University College",
        "district": "Mysore",
        "state": "Karnataka",
        "university": "Mysore University, Mysore (Id: U-0235)"
    },
    {
        "college_name": "COLLEGE OF AGRICULTURE (Id: C-33102)",
        "college_type": "Constituent / University College",
        "district": "Faizabad",
        "state": "Uttar Pradesh",
        "university": "Narendra Deo University of Agriculture & Technology, Faizabad (Id: U-0531)"
    },
    {
        "college_name": "COLLEGE OF FISHRIES (Id: C-33101)",
        "college_type": "Constituent / University College",
        "district": "Faizabad",
        "state": "Uttar Pradesh",
        "university": "Narendra Deo University of Agriculture & Technology, Faizabad (Id: U-0531)"
    },
    {
        "college_name": "COLLEGE OF HOME SCIENCE (Id: C-33097)",
        "college_type": "Constituent / University College",
        "district": "Faizabad",
        "state": "Uttar Pradesh",
        "university": "Narendra Deo University of Agriculture & Technology, Faizabad (Id: U-0531)"
    },
    {
        "college_name": "COLLEGE OF HORTICULTURE AND FORESTRY (Id: C-33095)",
        "college_type": "Constituent / University College",
        "district": "Faizabad",
        "state": "Uttar Pradesh",
        "university": "Narendra Deo University of Agriculture & Technology, Faizabad (Id: U-0531)"
    },
    {
        "college_name": "COLLEGE OF VETRINARY SCEINCE & ANIMAL HUSBANDARY (Id: C-33096)",
        "college_type": "Constituent / University College",
        "district": "Faizabad",
        "state": "Uttar Pradesh",
        "university": "Narendra Deo University of Agriculture & Technology, Faizabad (Id: U-0531)"
    },
    {
        "college_name": "DIRECTORATE OF AGRICULTURAL RESEARCH (Id: C-33098)",
        "college_type": "Constituent / University College",
        "district": "Faizabad",
        "state": "Uttar Pradesh",
        "university": "Narendra Deo University of Agriculture & Technology, Faizabad (Id: U-0531)"
    },
    {
        "college_name": "DIRECTORATE OF EXTENSION EDUCATION (Id: C-33100)",
        "college_type": "Constituent / University College",
        "district": "Faizabad",
        "state": "Uttar Pradesh",
        "university": "Narendra Deo University of Agriculture & Technology, Faizabad (Id: U-0531)"
    },
    {
        "college_name": "INSTITUTE OF BIODIVERSITY AND BIOTECHNOLOGY (Id: C-33099)",
        "college_type": "Constituent / University College",
        "district": "Faizabad",
        "state": "Uttar Pradesh",
        "university": "Narendra Deo University of Agriculture & Technology, Faizabad (Id: U-0531)"
    },
    {
        "college_name": "MAHAMAYA COLLEGE OF AGRICULTURAL ENGINEARING (Id: C-33094)",
        "college_type": "Constituent / University College",
        "district": "Ambedkar Nagar",
        "state": "Uttar Pradesh",
        "university": "Narendra Deo University of Agriculture & Technology, Faizabad (Id: U-0531)"
    },
    {
        "college_name": "ASPEE College of Horticulture and Forestry (Id: C-6593)",
        "college_type": "Constituent / University College",
        "district": "Navsari",
        "state": "Gujarat",
        "university": "Navsari Agricultural University (Id: U-0145)"
    },
    {
        "college_name": "ASPEE Institue of Agribussiness Management (Id: C-6591)",
        "college_type": "Constituent / University College",
        "district": "Navsari",
        "state": "Gujarat",
        "university": "Navsari Agricultural University (Id: U-0145)"
    },
    {
        "college_name": "COLLEGE OF AGRICULTURAL ENGINEERING, DEDIAPADA (Id: C-46336)",
        "college_type": "Constituent / University College",
        "district": "Narmada",
        "state": "Gujarat",
        "university": "Navsari Agricultural University (Id: U-0145)"
    },
    {
        "college_name": "COLLEGE OF AGRICULTURE, BHARUCH (Id: C-46334)",
        "college_type": "Constituent / University College",
        "district": "Bharuch",
        "state": "Gujarat",
        "university": "Navsari Agricultural University (Id: U-0145)"
    },
    {
        "college_name": "COLLEGE OF AGRICULTURE, WAGHAI (Id: C-46333)",
        "college_type": "Constituent / University College",
        "district": "The Dangs",
        "state": "Gujarat",
        "university": "Navsari Agricultural University (Id: U-0145)"
    },
    {
        "college_name": "GUJARAT AGRICULTURAL BIOTECH INSTITUTE, SURAT (Id: C-46335)",
        "college_type": "Constituent / University College",
        "district": "Surat",
        "state": "Gujarat",
        "university": "Navsari Agricultural University (Id: U-0145)"
    },
    {
        "college_name": "N.M.College of Agriculture (Id: C-6590)",
        "college_type": "Constituent / University College",
        "district": "Navsari",
        "state": "Gujarat",
        "university": "Navsari Agricultural University (Id: U-0145)"
    },
    {
        "college_name": "POLYTECHNIC IN AGRICULTURAL ENGINEERING, DEDIAPADA (Id: C-48405)",
        "college_type": "Constituent / University College",
        "district": "Narmada",
        "state": "Gujarat",
        "university": "Navsari Agricultural University (Id: U-0145)"
    },
    {
        "college_name": "POLYTECHNIC IN AGRICULTURE, CO-OPERATION, BANKING AND MARKETING, WAGHAI (Id: C-48408)",
        "college_type": "Constituent / University College",
        "district": "The Dangs",
        "state": "Gujarat",
        "university": "Navsari Agricultural University (Id: U-0145)"
    },
    {
        "college_name": "POLYTECHNIC IN AGRICULTURE, MAKTAMPUR (Id: C-48406)",
        "college_type": "Constituent / University College",
        "district": "Bharuch",
        "state": "Gujarat",
        "university": "Navsari Agricultural University (Id: U-0145)"
    },
    {
        "college_name": "POLYTECHNIC IN AGRICULTURE, VYARA (Id: C-48407)",
        "college_type": "Constituent / University College",
        "district": "Tapi",
        "state": "Gujarat",
        "university": "Navsari Agricultural University (Id: U-0145)"
    },
    {
        "college_name": "POLYTECHNIC IN ANIMAL HUSBANDARY, NAVSARI (Id: C-48410)",
        "college_type": "Constituent / University College",
        "district": "Navsari",
        "state": "Gujarat",
        "university": "Navsari Agricultural University (Id: U-0145)"
    },
    {
        "college_name": "POLYTECHNIC IN HORTICULTURE, NAVSARI (Id: C-48409)",
        "college_type": "Constituent / University College",
        "district": "Navsari",
        "state": "Gujarat",
        "university": "Navsari Agricultural University (Id: U-0145)"
    },
    {
        "college_name": "POLYTECHNIC IN HORTICULTURE, PARIA (Id: C-48411)",
        "college_type": "Constituent / University College",
        "district": "Valsad",
        "state": "Gujarat",
        "university": "Navsari Agricultural University (Id: U-0145)"
    },
    {
        "college_name": "Vanbandhu College of Veterinary Science and Animal Husbandry (Id: C-6592)",
        "college_type": "Constituent / University College",
        "district": "Navsari",
        "state": "Gujarat",
        "university": "Navsari Agricultural University (Id: U-0145)"
    },
    {
        "college_name": "G.L.A. College,Medininagar (Id: C-42762)",
        "college_type": "Constituent / University College",
        "district": "Palamu",
        "state": "Jharkhand",
        "university": "Nilamber-Pitamber University, Palamu (Id: U-0208)"
    },
    {
        "college_name": "J.S.College,medininnagar (Id: C-42750)",
        "college_type": "Constituent / University College",
        "district": "Palamu",
        "state": "Jharkhand",
        "university": "Nilamber-Pitamber University, Palamu (Id: U-0208)"
    },
    {
        "college_name": "S.S.J.S.N. College,Garhwa (Id: C-42766)",
        "college_type": "Constituent / University College",
        "district": "Garhwa",
        "state": "Jharkhand",
        "university": "Nilamber-Pitamber University, Palamu (Id: U-0208)"
    },
    {
        "college_name": "Y.S.N.M.College,Medininnagar (Id: C-42754)",
        "college_type": "Constituent / University College",
        "district": "Palamu",
        "state": "Jharkhand",
        "university": "Nilamber-Pitamber University, Palamu (Id: U-0208)"
    },
    {
        "college_name": "Institute of Diploma studies, Nirma University (Id: C-438)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Nirma University, Ahmedabad (Id: U-0146)"
    },
    {
        "college_name": "Institute of Law, Nirma University (Id: C-435)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Nirma University, Ahmedabad (Id: U-0146)"
    },
    {
        "college_name": "Institute of Management, Nirma University (Id: C-437)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Nirma University, Ahmedabad (Id: U-0146)"
    },
    {
        "college_name": "Institute of Pharmacy, Nirma University (Id: C-436)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Nirma University, Ahmedabad (Id: U-0146)"
    },
    {
        "college_name": "Institute of Science, Nirma University (Id: C-440)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Nirma University, Ahmedabad (Id: U-0146)"
    },
    {
        "college_name": "Institute of Technology, Nirma University (Id: C-439)",
        "college_type": "Constituent / University College",
        "district": "Ahmadabad",
        "state": "Gujarat",
        "university": "Nirma University, Ahmedabad (Id: U-0146)"
    },
    {
        "college_name": "A.B.S.M. INSTITUTE OF DENTAL SCIENCES (Id: C-19320)",
        "college_type": "Constituent / University College",
        "district": "Dakshina Kannada",
        "state": "Karnataka",
        "university": "NITTE Unversity, Mangalore (Id: U-0239)"
    },
    {
        "college_name": "DEPARTMENT OF MASS COMMUNICATION & JOURNALISM (Id: C-48491)",
        "college_type": "Constituent / University College",
        "district": "Dakshina Kannada",
        "state": "Karnataka",
        "university": "NITTE Unversity, Mangalore (Id: U-0239)"
    },
    {
        "college_name": "K. S. HEGDE MEDICAL ACADEMY (Id: C-19319)",
        "college_type": "Constituent / University College",
        "district": "Dakshina Kannada",
        "state": "Karnataka",
        "university": "NITTE Unversity, Mangalore (Id: U-0239)"
    },
    {
        "college_name": "N.G.S.M. INSTITUTE OF PHARMACEUTICAL SCIENCES (Id: C-19322)",
        "college_type": "Constituent / University College",
        "district": "Dakshina Kannada",
        "state": "Karnataka",
        "university": "NITTE Unversity, Mangalore (Id: U-0239)"
    },
    {
        "college_name": "NITTE INSTITUTE OF PHYSIOTHERAPY (Id: C-19321)",
        "college_type": "Constituent / University College",
        "district": "Dakshina Kannada",
        "state": "Karnataka",
        "university": "NITTE Unversity, Mangalore (Id: U-0239)"
    },
    {
        "college_name": "NITTE USHA INSTITUTE OF NURSING SCIENCES (Id: C-19318)",
        "college_type": "Constituent / University College",
        "district": "Dakshina Kannada",
        "state": "Karnataka",
        "university": "NITTE Unversity, Mangalore (Id: U-0239)"
    },
    {
        "college_name": "A B N SEAL COLLEGE, COOCHBEHAR (Id: C-45314)",
        "college_type": "Constituent / University College",
        "district": "Koch Bihar",
        "state": "West Bengal",
        "university": "North Bengal University, Darjeeling (Id: U-0579)"
    },
    {
        "college_name": "ANANDA CHANDRA COLLEGE, JALPAIGURI (Id: C-45354)",
        "college_type": "Constituent / University College",
        "district": "Jalpaiguri",
        "state": "West Bengal",
        "university": "North Bengal University, Darjeeling (Id: U-0579)"
    },
    {
        "college_name": "DARJEELING GOVERNMENT COLLEGE, DARJEELING (Id: C-45333)",
        "college_type": "Constituent / University College",
        "district": "Darjiling",
        "state": "West Bengal",
        "university": "North Bengal University, Darjeeling (Id: U-0579)"
    },
    {
        "college_name": "RAIGANJ COLLEGE (UNIVERSITY COLLEGE), UTTAR DINAJPUR (Id: C-45789)",
        "college_type": "Constituent / University College",
        "district": "Uttar Dinajpur",
        "state": "West Bengal",
        "university": "North Bengal University, Darjeeling (Id: U-0579)"
    },
    {
        "college_name": "ST JOSEPH COLLEGE, DARJEELING (Id: C-45349)",
        "college_type": "Constituent / University College",
        "district": "Darjiling",
        "state": "West Bengal",
        "university": "North Bengal University, Darjeeling (Id: U-0579)"
    },
    {
        "college_name": "College of Agricultural Engineering & Technology, Bhubaneswar (Id: C-21470)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Orissa University of Agriculture & Technology, Bhubaneswar (Id: U-0360)"
    },
    {
        "college_name": "College of Agriculture, Bhawanipatna (Id: C-21467)",
        "college_type": "Constituent / University College",
        "district": "Kalahandi",
        "state": "Odisha",
        "university": "Orissa University of Agriculture & Technology, Bhubaneswar (Id: U-0360)"
    },
    {
        "college_name": "College of Agriculture, Bhubaneswar (Id: C-21462)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Orissa University of Agriculture & Technology, Bhubaneswar (Id: U-0360)"
    },
    {
        "college_name": "College of Agriculture, Chiplima (Id: C-21464)",
        "college_type": "Constituent / University College",
        "district": "Sambalpur",
        "state": "Odisha",
        "university": "Orissa University of Agriculture & Technology, Bhubaneswar (Id: U-0360)"
    },
    {
        "college_name": "College of Basic Science & Humanities, Bhubaneswar (Id: C-21463)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Orissa University of Agriculture & Technology, Bhubaneswar (Id: U-0360)"
    },
    {
        "college_name": "College of Fisheries, Rangailunda (Id: C-21460)",
        "college_type": "Constituent / University College",
        "district": "Ganjam",
        "state": "Odisha",
        "university": "Orissa University of Agriculture & Technology, Bhubaneswar (Id: U-0360)"
    },
    {
        "college_name": "College of Forestry, Bhubaneswar (Id: C-21461)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Orissa University of Agriculture & Technology, Bhubaneswar (Id: U-0360)"
    },
    {
        "college_name": "College of Home Science, Bhubaneswar (Id: C-21469)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Orissa University of Agriculture & Technology, Bhubaneswar (Id: U-0360)"
    },
    {
        "college_name": "College of Horticulture, Chiplima (Id: C-21466)",
        "college_type": "Constituent / University College",
        "district": "Sambalpur",
        "state": "Odisha",
        "university": "Orissa University of Agriculture & Technology, Bhubaneswar (Id: U-0360)"
    },
    {
        "college_name": "College of Veterinary Science & Animal Husbandry, Bhubaneswar (Id: C-21465)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Orissa University of Agriculture & Technology, Bhubaneswar (Id: U-0360)"
    },
    {
        "college_name": "Nizam College, Basheerbagh (Id: C-25476)",
        "college_type": "Constituent / University College",
        "district": "Hyderabad",
        "state": "Telangana",
        "university": "Osmania University, Hyderabad (Id: U-0027)"
    },
    {
        "college_name": "P.G. College of Law, Basheerbagh (Id: C-26025)",
        "college_type": "Constituent / University College",
        "district": "Hyderabad",
        "state": "Telangana",
        "university": "Osmania University, Hyderabad (Id: U-0027)"
    },
    {
        "college_name": "P.G. College, Secunderabad (Id: C-25883)",
        "college_type": "Constituent / University College",
        "district": "Hyderabad",
        "state": "Telangana",
        "university": "Osmania University, Hyderabad (Id: U-0027)"
    },
    {
        "college_name": "University College for Women, Koti (Id: C-25938)",
        "college_type": "Constituent / University College",
        "district": "Hyderabad",
        "state": "Telangana",
        "university": "Osmania University, Hyderabad (Id: U-0027)"
    },
    {
        "college_name": "University College of Science, Saifabad (Id: C-25761)",
        "college_type": "Constituent / University College",
        "district": "Hyderabad",
        "state": "Telangana",
        "university": "Osmania University, Hyderabad (Id: U-0027)"
    },
    {
        "college_name": "Department of Biotechnology and Bioinformatics (Id: C-10972)",
        "college_type": "Constituent / University College",
        "district": "Thane",
        "state": "Maharashtra",
        "university": "Padmashree Dr. D. Y. Patil Vidyapeeth, , Mumbai (Id: U-0321)"
    },
    {
        "college_name": "Department of Business Management (Id: C-10973)",
        "college_type": "Constituent / University College",
        "district": "Thane",
        "state": "Maharashtra",
        "university": "Padmashree Dr. D. Y. Patil Vidyapeeth, , Mumbai (Id: U-0321)"
    },
    {
        "college_name": "Department of Education (Id: C-10978)",
        "college_type": "Constituent / University College",
        "district": "Thane",
        "state": "Maharashtra",
        "university": "Padmashree Dr. D. Y. Patil Vidyapeeth, , Mumbai (Id: U-0321)"
    },
    {
        "college_name": "Department of Hospitality and Tourism Studies (Id: C-10979)",
        "college_type": "Constituent / University College",
        "district": "Thane",
        "state": "Maharashtra",
        "university": "Padmashree Dr. D. Y. Patil Vidyapeeth, , Mumbai (Id: U-0321)"
    },
    {
        "college_name": "Department of Physiotherapy (Id: C-10977)",
        "college_type": "Constituent / University College",
        "district": "Thane",
        "state": "Maharashtra",
        "university": "Padmashree Dr. D. Y. Patil Vidyapeeth, , Mumbai (Id: U-0321)"
    },
    {
        "college_name": "Dr.D.Y.Patil College of Ayurved and Research Institute (Id: C-10976)",
        "college_type": "Constituent / University College",
        "district": "Thane",
        "state": "Maharashtra",
        "university": "Padmashree Dr. D. Y. Patil Vidyapeeth, , Mumbai (Id: U-0321)"
    },
    {
        "college_name": "Dr.D.Y.Patil Dental College and Hospital (Id: C-10975)",
        "college_type": "Constituent / University College",
        "district": "Thane",
        "state": "Maharashtra",
        "university": "Padmashree Dr. D. Y. Patil Vidyapeeth, , Mumbai (Id: U-0321)"
    },
    {
        "college_name": "Dr.D.Y.Patil Medical College, Hospital and Research Centre (Id: C-10974)",
        "college_type": "Constituent / University College",
        "district": "Thane",
        "state": "Maharashtra",
        "university": "Padmashree Dr. D. Y. Patil Vidyapeeth, , Mumbai (Id: U-0321)"
    },
    {
        "college_name": "Palamuru University (Id: C-21972)",
        "college_type": "Constituent / University College",
        "district": "Mahbubnagar",
        "state": "Telangana",
        "university": "Palamuru University, Mahabubnagar (Id: U-0028)"
    },
    {
        "college_name": "School of Liberal Studies (Id: C-10231)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Pandit Deendayal Petroleum University, Gandhi Nagar (Id: U-0147)"
    },
    {
        "college_name": "School of Nuclear Energy (Id: C-10229)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Pandit Deendayal Petroleum University, Gandhi Nagar (Id: U-0147)"
    },
    {
        "college_name": "School of Petroleum Management (Id: C-10234)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Pandit Deendayal Petroleum University, Gandhi Nagar (Id: U-0147)"
    },
    {
        "college_name": "School of Petroleum Technology (Id: C-10230)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Pandit Deendayal Petroleum University, Gandhi Nagar (Id: U-0147)"
    },
    {
        "college_name": "School of Solar Energy (Id: C-10233)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Pandit Deendayal Petroleum University, Gandhi Nagar (Id: U-0147)"
    },
    {
        "college_name": "School of Technology (Id: C-10232)",
        "college_type": "Constituent / University College",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "university": "Pandit Deendayal Petroleum University, Gandhi Nagar (Id: U-0147)"
    },
    {
        "college_name": "University College, Balachaur, Nawanshehar (Id: C-29371)",
        "college_type": "Constituent / University College",
        "district": "Shahid Bhagat Singh Nagar",
        "state": "Punjab",
        "university": "Panjab University,Chandigarh (Id: U-0078)"
    },
    {
        "college_name": "University College, Guru Har Sahai, Firozpur (Id: C-31040)",
        "college_type": "Constituent / University College",
        "district": "Firozpur",
        "state": "Punjab",
        "university": "Panjab University,Chandigarh (Id: U-0078)"
    },
    {
        "college_name": "University College, Nihal Singh Wala, Moga (Id: C-29417)",
        "college_type": "Constituent / University College",
        "district": "Moga",
        "state": "Punjab",
        "university": "Panjab University,Chandigarh (Id: U-0078)"
    },
    {
        "college_name": "University College, Sikhwala, Muktsar (Id: C-29265)",
        "college_type": "Constituent / University College",
        "district": "Muktsar",
        "state": "Punjab",
        "university": "Panjab University,Chandigarh (Id: U-0078)"
    },
    {
        "college_name": "Bihar College of Physiotherapy & Occupational Therapy (Id: C-43234)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Patna University, Patna (Id: U-0074)"
    },
    {
        "college_name": "Bihar National College (Id: C-22855)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Patna University, Patna (Id: U-0074)"
    },
    {
        "college_name": "College of Arts & Craft (Id: C-22852)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Patna University, Patna (Id: U-0074)"
    },
    {
        "college_name": "Magadh Mahila College (Id: C-22851)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Patna University, Patna (Id: U-0074)"
    },
    {
        "college_name": "Patna College (Id: C-22858)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Patna University, Patna (Id: U-0074)"
    },
    {
        "college_name": "Patna Law College (Id: C-22854)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Patna University, Patna (Id: U-0074)"
    },
    {
        "college_name": "Patna Science College (Id: C-22853)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Patna University, Patna (Id: U-0074)"
    },
    {
        "college_name": "Patna Training College (Id: C-35448)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Patna University, Patna (Id: U-0074)"
    },
    {
        "college_name": "Patna Women's College (Id: C-22850)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Patna University, Patna (Id: U-0074)"
    },
    {
        "college_name": "Vanijya Mahavidayala (Id: C-35447)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Patna University, Patna (Id: U-0074)"
    },
    {
        "college_name": "Women's Training College (Id: C-35449)",
        "college_type": "Constituent / University College",
        "district": "Patna",
        "state": "Bihar",
        "university": "Patna University, Patna (Id: U-0074)"
    },
    {
        "college_name": "PERIYAR UNIVERSITY COLLEGE OF ARTS AND SCIENCE, IDAPPADI (Id: C-47502)",
        "college_type": "Constituent / University College",
        "district": "Salem",
        "state": "Tamil Nadu",
        "university": "Periyar University, Salem (Id: U-0470)"
    },
    {
        "college_name": "Periyar University College of Arts & Science,pappirettipatty (Id: C-9507)",
        "college_type": "Constituent / University College",
        "district": "Dharmapuri",
        "state": "Tamil Nadu",
        "university": "Periyar University, Salem (Id: U-0470)"
    },
    {
        "college_name": "Periyar University College of Arts & Science,pennagaram (Id: C-9501)",
        "college_type": "Constituent / University College",
        "district": "Dharmapuri",
        "state": "Tamil Nadu",
        "university": "Periyar University, Salem (Id: U-0470)"
    },
    {
        "college_name": "Pondicherry University Community College (Id: C-6514)",
        "college_type": "Constituent / University College",
        "district": "Puducherry",
        "state": "Puducherry",
        "university": "Pondicherry Univeristy, Puducherry (Id: U-0369)"
    },
    {
        "college_name": "Center for Biotechnology, Loni (Id: C-9769)",
        "college_type": "Constituent / University College",
        "district": "Ahmadnagar",
        "state": "Maharashtra",
        "university": "Pravara Institute of Medical Sciences, Ahmednagar (Id: U-0322)"
    },
    {
        "college_name": "Center for Social Medicine, Loni (Id: C-9770)",
        "college_type": "Constituent / University College",
        "district": "Ahmadnagar",
        "state": "Maharashtra",
        "university": "Pravara Institute of Medical Sciences, Ahmednagar (Id: U-0322)"
    },
    {
        "college_name": "College of Nursing, Loni (Id: C-9768)",
        "college_type": "Constituent / University College",
        "district": "Ahmadnagar",
        "state": "Maharashtra",
        "university": "Pravara Institute of Medical Sciences, Ahmednagar (Id: U-0322)"
    },
    {
        "college_name": "College of Physiotherapy, Loni (Id: C-9766)",
        "college_type": "Constituent / University College",
        "district": "Ahmadnagar",
        "state": "Maharashtra",
        "university": "Pravara Institute of Medical Sciences, Ahmednagar (Id: U-0322)"
    },
    {
        "college_name": "Rural Dental College, Loni (Id: C-9764)",
        "college_type": "Constituent / University College",
        "district": "Ahmadnagar",
        "state": "Maharashtra",
        "university": "Pravara Institute of Medical Sciences, Ahmednagar (Id: U-0322)"
    },
    {
        "college_name": "Rural Medical College, Loni (Id: C-9767)",
        "college_type": "Constituent / University College",
        "district": "Ahmadnagar",
        "state": "Maharashtra",
        "university": "Pravara Institute of Medical Sciences, Ahmednagar (Id: U-0322)"
    },
    {
        "college_name": "College of B.P.T. , Pt. B.D.Sharma, PGIMS, Rohtak (Id: C-30737)",
        "college_type": "Constituent / University College",
        "district": "Rohtak",
        "state": "Haryana",
        "university": "Pt. Bhagat Dyal University of Health Science, Rohtak (Id: U-0174)"
    },
    {
        "college_name": "College of Nursing, Pt. B.D.Sharma , PGIMS, Rohtak (Id: C-30766)",
        "college_type": "Constituent / University College",
        "district": "Rohtak",
        "state": "Haryana",
        "university": "Pt. Bhagat Dyal University of Health Science, Rohtak (Id: U-0174)"
    },
    {
        "college_name": "College of Pharmacy, Pt. B.D.Sharma, PGIMS, Rohtak (Id: C-30768)",
        "college_type": "Constituent / University College",
        "district": "Rohtak",
        "state": "Haryana",
        "university": "Pt. Bhagat Dyal University of Health Science, Rohtak (Id: U-0174)"
    },
    {
        "college_name": "Govt. Dental College, Rohtak (Id: C-30756)",
        "college_type": "Constituent / University College",
        "district": "Rohtak",
        "state": "Haryana",
        "university": "Pt. Bhagat Dyal University of Health Science, Rohtak (Id: U-0174)"
    },
    {
        "college_name": "Pt. B.D.Sharma , PGIMS , Rohtak (Id: C-30767)",
        "college_type": "Constituent / University College",
        "district": "Rohtak",
        "state": "Haryana",
        "university": "Pt. Bhagat Dyal University of Health Science, Rohtak (Id: U-0174)"
    },
    {
        "college_name": "PUNJABI UNIVERSITY COLLEGE, MEERAPUR (Id: C-48370)",
        "college_type": "Constituent / University College",
        "district": "Patiala",
        "state": "Punjab",
        "university": "Punjabi University, Patiala (Id: U-0383)"
    },
    {
        "college_name": "S. Balraj Singh Bhundarh Memorial university College Sadulgarh (Id: C-22286)",
        "college_type": "Constituent / University College",
        "district": "Mansa",
        "state": "Punjab",
        "university": "Punjabi University, Patiala (Id: U-0383)"
    },
    {
        "college_name": "University College, Chunni Kalan (Id: C-22245)",
        "college_type": "Constituent / University College",
        "district": "Fatehgarh Sahib",
        "state": "Punjab",
        "university": "Punjabi University, Patiala (Id: U-0383)"
    },
    {
        "college_name": "University College, Dhilwan (Id: C-22090)",
        "college_type": "Constituent / University College",
        "district": "Barnala",
        "state": "Punjab",
        "university": "Punjabi University, Patiala (Id: U-0383)"
    },
    {
        "college_name": "University College, Ghanaur (Id: C-22244)",
        "college_type": "Constituent / University College",
        "district": "Patiala",
        "state": "Punjab",
        "university": "Punjabi University, Patiala (Id: U-0383)"
    },
    {
        "college_name": "University College, Ghudda (Id: C-22154)",
        "college_type": "Constituent / University College",
        "district": "Bathinda",
        "state": "Punjab",
        "university": "Punjabi University, Patiala (Id: U-0383)"
    },
    {
        "college_name": "University College, Jaitu (Id: C-22181)",
        "college_type": "Constituent / University College",
        "district": "Faridkot",
        "state": "Punjab",
        "university": "Punjabi University, Patiala (Id: U-0383)"
    },
    {
        "college_name": "University College, Moonak (Id: C-22177)",
        "college_type": "Constituent / University College",
        "district": "Sangrur",
        "state": "Punjab",
        "university": "Punjabi University, Patiala (Id: U-0383)"
    },
    {
        "college_name": "Government Music College, satna (Id: C-29544)",
        "college_type": "Constituent / University College",
        "district": "Satna",
        "state": "Madhya Pradesh",
        "university": "Raja Mansingh Tomar Music & Arts University, Gwalior (Id: U-0629)"
    },
    {
        "college_name": "Govt. Anand Sangeet Mahavidhyalaya, dhar (Id: C-29521)",
        "college_type": "Constituent / University College",
        "district": "Dhar",
        "state": "Madhya Pradesh",
        "university": "Raja Mansingh Tomar Music & Arts University, Gwalior (Id: U-0629)"
    },
    {
        "college_name": "Govt. Institute of Fine Art, indore (Id: C-29510)",
        "college_type": "Constituent / University College",
        "district": "Indore",
        "state": "Madhya Pradesh",
        "university": "Raja Mansingh Tomar Music & Arts University, Gwalior (Id: U-0629)"
    },
    {
        "college_name": "Govt. Institute of Fine Art, jabalpur (Id: C-29497)",
        "college_type": "Constituent / University College",
        "district": "Jabalpur",
        "state": "Madhya Pradesh",
        "university": "Raja Mansingh Tomar Music & Arts University, Gwalior (Id: U-0629)"
    },
    {
        "college_name": "Govt. Institute of Fine Arts, dhar (Id: C-29494)",
        "college_type": "Constituent / University College",
        "district": "Dhar",
        "state": "Madhya Pradesh",
        "university": "Raja Mansingh Tomar Music & Arts University, Gwalior (Id: U-0629)"
    },
    {
        "college_name": "Govt. Institute of Fine Arts, gwalior (Id: C-29478)",
        "college_type": "Constituent / University College",
        "district": "Gwalior",
        "state": "Madhya Pradesh",
        "university": "Raja Mansingh Tomar Music & Arts University, Gwalior (Id: U-0629)"
    },
    {
        "college_name": "Govt. Institute of Fine Arts, indore (Id: C-29533)",
        "college_type": "Constituent / University College",
        "district": "Indore",
        "state": "Madhya Pradesh",
        "university": "Raja Mansingh Tomar Music & Arts University, Gwalior (Id: U-0629)"
    },
    {
        "college_name": "Govt. Madhav Sangeet College, gwalior (Id: C-29498)",
        "college_type": "Constituent / University College",
        "district": "Gwalior",
        "state": "Madhya Pradesh",
        "university": "Raja Mansingh Tomar Music & Arts University, Gwalior (Id: U-0629)"
    },
    {
        "college_name": "Govt. Madhav sangeet College, ujjain (Id: C-29568)",
        "college_type": "Constituent / University College",
        "district": "Ujjain",
        "state": "Madhya Pradesh",
        "university": "Raja Mansingh Tomar Music & Arts University, Gwalior (Id: U-0629)"
    },
    {
        "college_name": "Govt. Music College, mandsaur (Id: C-29571)",
        "college_type": "Constituent / University College",
        "district": "Mandsaur",
        "state": "Madhya Pradesh",
        "university": "Raja Mansingh Tomar Music & Arts University, Gwalior (Id: U-0629)"
    },
    {
        "college_name": "Govt. Music College, Narsinghpur (Id: C-29524)",
        "college_type": "Constituent / University College",
        "district": "Narsimhapur",
        "state": "Madhya Pradesh",
        "university": "Raja Mansingh Tomar Music & Arts University, Gwalior (Id: U-0629)"
    },
    {
        "college_name": "University Ayurved Nursing Training Centre, Jodhpur (Id: C-26246)",
        "college_type": "Constituent / University College",
        "district": "Jodhpur",
        "state": "Rajasthan",
        "university": "Rajasthan Ayurveda University, Jodhpur (Id: U-0418)"
    },
    {
        "college_name": "University College of Ayurved, Jodhpur (Id: C-26210)",
        "college_type": "Constituent / University College",
        "district": "Jodhpur",
        "state": "Rajasthan",
        "university": "Rajasthan Ayurveda University, Jodhpur (Id: U-0418)"
    },
    {
        "college_name": "Univeristy College of Engineering (Id: C-25225)",
        "college_type": "Constituent / University College",
        "district": "Kota",
        "state": "Rajasthan",
        "university": "Rajasthan Technical University, Kota (Id: U-0419)"
    },
    {
        "college_name": "Five Years Int. Law College, Jaipur (Id: C-38738)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "Rajasthan University, Jaipur (Id: U-0422)"
    },
    {
        "college_name": "University Commerce College, Jaipur (Id: C-39016)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "Rajasthan University, Jaipur (Id: U-0422)"
    },
    {
        "college_name": "University Law College IInd, Jaipur (Id: C-38910)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "Rajasthan University, Jaipur (Id: U-0422)"
    },
    {
        "college_name": "University Law College Ist, Jaipur (Id: C-38693)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "Rajasthan University, Jaipur (Id: U-0422)"
    },
    {
        "college_name": "University Maharaja College, Jaipur (Id: C-38254)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "Rajasthan University, Jaipur (Id: U-0422)"
    },
    {
        "college_name": "University Maharani's College, Jaipur (Id: C-38920)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "Rajasthan University, Jaipur (Id: U-0422)"
    },
    {
        "college_name": "University Rajasthan College, Jaipur (Id: C-38544)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "Rajasthan University, Jaipur (Id: U-0422)"
    },
    {
        "college_name": "College of Veterinary and Animal Science, Bikaner (Id: C-24511)",
        "college_type": "Constituent / University College",
        "district": "Bikaner",
        "state": "Rajasthan",
        "university": "Rajasthan University of Veterinary and Animal Sciences, Bikaner (Id: U-0421)"
    },
    {
        "college_name": "College of Veterinary and Animal Science, Navania, Udaipur (Id: C-37136)",
        "college_type": "Constituent / University College",
        "district": "Udaipur",
        "state": "Rajasthan",
        "university": "Rajasthan University of Veterinary and Animal Sciences, Bikaner (Id: U-0421)"
    },
    {
        "college_name": "College of Agricultural Engineering,Pusa (Id: C-10243)",
        "college_type": "Constituent / University College",
        "district": "Samastipur",
        "state": "Bihar",
        "university": "Rajendra Agricultural University, Samastipur (Id: U-0075)"
    },
    {
        "college_name": "College of Fisheries, Dholi (Id: C-10239)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Rajendra Agricultural University, Samastipur (Id: U-0075)"
    },
    {
        "college_name": "College of Home Science,Pusa (Id: C-10244)",
        "college_type": "Constituent / University College",
        "district": "Samastipur",
        "state": "Bihar",
        "university": "Rajendra Agricultural University, Samastipur (Id: U-0075)"
    },
    {
        "college_name": "Faculty of Basic Sciences and Humanities,Pusa (Id: C-10240)",
        "college_type": "Constituent / University College",
        "district": "Samastipur",
        "state": "Bihar",
        "university": "Rajendra Agricultural University, Samastipur (Id: U-0075)"
    },
    {
        "college_name": "Tirhut College of Agricultural ,Dholi (Id: C-10241)",
        "college_type": "Constituent / University College",
        "district": "Muzaffarpur",
        "state": "Bihar",
        "university": "Rajendra Agricultural University, Samastipur (Id: U-0075)"
    },
    {
        "college_name": "University Institute of Technology, RGPV (Id: C-35953)",
        "college_type": "Constituent / University College",
        "district": "Bhopal",
        "state": "Madhya Pradesh",
        "university": "Rajiv Gandhi Prodoyogiki Vishwavidyalaya, Bhopal (Id: U-0287)"
    },
    {
        "college_name": "University Polytechnic, RGPV (Id: C-36082)",
        "college_type": "Constituent / University College",
        "district": "Bhopal",
        "state": "Madhya Pradesh",
        "university": "Rajiv Gandhi Prodoyogiki Vishwavidyalaya, Bhopal (Id: U-0287)"
    },
    {
        "college_name": "BHAGWANT RAO MANDALOI, COLLEGE OF AGRICULTURE, KHANDWA (Id: C-45271)",
        "college_type": "Constituent / University College",
        "district": "Khandwa",
        "state": "Madhya Pradesh",
        "university": "Rajmata Vijayaraje Scindia Krishi Vishwa Vidyalaya, Gwalior (Id: U-0288)"
    },
    {
        "college_name": "COLLEGE OF AGRICULTURE, GWALIOR (Id: C-45268)",
        "college_type": "Constituent / University College",
        "district": "Gwalior",
        "state": "Madhya Pradesh",
        "university": "Rajmata Vijayaraje Scindia Krishi Vishwa Vidyalaya, Gwalior (Id: U-0288)"
    },
    {
        "college_name": "COLLEGE OF AGRICULTURE, INDORE (Id: C-45269)",
        "college_type": "Constituent / University College",
        "district": "Indore",
        "state": "Madhya Pradesh",
        "university": "Rajmata Vijayaraje Scindia Krishi Vishwa Vidyalaya, Gwalior (Id: U-0288)"
    },
    {
        "college_name": "KNK COLLEGE OF HORTICULTURE, MANDSAUR (Id: C-45272)",
        "college_type": "Constituent / University College",
        "district": "Mandsaur",
        "state": "Madhya Pradesh",
        "university": "Rajmata Vijayaraje Scindia Krishi Vishwa Vidyalaya, Gwalior (Id: U-0288)"
    },
    {
        "college_name": "R A K COLLEGE OF AGRICULTURE, SEHORE (Id: C-45270)",
        "college_type": "Constituent / University College",
        "district": "Sehore",
        "state": "Madhya Pradesh",
        "university": "Rajmata Vijayaraje Scindia Krishi Vishwa Vidyalaya, Gwalior (Id: U-0288)"
    },
    {
        "college_name": "Birsa College (Id: C-15047)",
        "college_type": "Constituent / University College",
        "district": "Khunti",
        "state": "Jharkhand",
        "university": "Ranchi University, Ranchi (Id: U-0209)"
    },
    {
        "college_name": "B. N. J. College, Sisai (Id: C-15043)",
        "college_type": "Constituent / University College",
        "district": "Gumla",
        "state": "Jharkhand",
        "university": "Ranchi University, Ranchi (Id: U-0209)"
    },
    {
        "college_name": "B. S. College (Id: C-15044)",
        "college_type": "Constituent / University College",
        "district": "Lohardaga",
        "state": "Jharkhand",
        "university": "Ranchi University, Ranchi (Id: U-0209)"
    },
    {
        "college_name": "Doranda College (Id: C-15050)",
        "college_type": "Constituent / University College",
        "district": "Ranchi",
        "state": "Jharkhand",
        "university": "Ranchi University, Ranchi (Id: U-0209)"
    },
    {
        "college_name": "J. N. College (Id: C-15056)",
        "college_type": "Constituent / University College",
        "district": "Ranchi",
        "state": "Jharkhand",
        "university": "Ranchi University, Ranchi (Id: U-0209)"
    },
    {
        "college_name": "K. C. Bhagat College, Bero (Id: C-15068)",
        "college_type": "Constituent / University College",
        "district": "Ranchi",
        "state": "Jharkhand",
        "university": "Ranchi University, Ranchi (Id: U-0209)"
    },
    {
        "college_name": "K. O. College (Id: C-15063)",
        "college_type": "Constituent / University College",
        "district": "Gumla",
        "state": "Jharkhand",
        "university": "Ranchi University, Ranchi (Id: U-0209)"
    },
    {
        "college_name": "Mandar College, Mandar (Id: C-15072)",
        "college_type": "Constituent / University College",
        "district": "Ranchi",
        "state": "Jharkhand",
        "university": "Ranchi University, Ranchi (Id: U-0209)"
    },
    {
        "college_name": "Marwari College (Id: C-15064)",
        "college_type": "Constituent / University College",
        "district": "Ranchi",
        "state": "Jharkhand",
        "university": "Ranchi University, Ranchi (Id: U-0209)"
    },
    {
        "college_name": "P. P. K. College, Bundu (Id: C-15048)",
        "college_type": "Constituent / University College",
        "district": "Ranchi",
        "state": "Jharkhand",
        "university": "Ranchi University, Ranchi (Id: U-0209)"
    },
    {
        "college_name": "Ranchi College (Id: C-15061)",
        "college_type": "Constituent / University College",
        "district": "Ranchi",
        "state": "Jharkhand",
        "university": "Ranchi University, Ranchi (Id: U-0209)"
    },
    {
        "college_name": "Ranchi Women's College (Id: C-15051)",
        "college_type": "Constituent / University College",
        "district": "Ranchi",
        "state": "Jharkhand",
        "university": "Ranchi University, Ranchi (Id: U-0209)"
    },
    {
        "college_name": "R. L. S. Y. College (Id: C-15062)",
        "college_type": "Constituent / University College",
        "district": "Ranchi",
        "state": "Jharkhand",
        "university": "Ranchi University, Ranchi (Id: U-0209)"
    },
    {
        "college_name": "Simdega College (Id: C-15074)",
        "college_type": "Constituent / University College",
        "district": "Simdega",
        "state": "Jharkhand",
        "university": "Ranchi University, Ranchi (Id: U-0209)"
    },
    {
        "college_name": "S. S. Memorial College (Id: C-15059)",
        "college_type": "Constituent / University College",
        "district": "Ranchi",
        "state": "Jharkhand",
        "university": "Ranchi University, Ranchi (Id: U-0209)"
    },
    {
        "college_name": "School of Computer Science (Id: C-45103)",
        "college_type": "Constituent / University College",
        "district": "Rajkot",
        "state": "Gujarat",
        "university": "R K University, Rajkot (Id: U-0647)"
    },
    {
        "college_name": "School of Diploma Studies (Id: C-33)",
        "college_type": "Constituent / University College",
        "district": "Rajkot",
        "state": "Gujarat",
        "university": "R K University, Rajkot (Id: U-0647)"
    },
    {
        "college_name": "School of Engineering (Id: C-130)",
        "college_type": "Constituent / University College",
        "district": "Rajkot",
        "state": "Gujarat",
        "university": "R K University, Rajkot (Id: U-0647)"
    },
    {
        "college_name": "School of Management (Id: C-101)",
        "college_type": "Constituent / University College",
        "district": "Rajkot",
        "state": "Gujarat",
        "university": "R K University, Rajkot (Id: U-0647)"
    },
    {
        "college_name": "School of Pharmacy (Id: C-355)",
        "college_type": "Constituent / University College",
        "district": "Rajkot",
        "state": "Gujarat",
        "university": "R K University, Rajkot (Id: U-0647)"
    },
    {
        "college_name": "School of Physiotherapy (Id: C-773)",
        "college_type": "Constituent / University College",
        "district": "Rajkot",
        "state": "Gujarat",
        "university": "R K University, Rajkot (Id: U-0647)"
    },
    {
        "college_name": "School of Science (Id: C-45104)",
        "college_type": "Constituent / University College",
        "district": "Rajkot",
        "state": "Gujarat",
        "university": "R K University, Rajkot (Id: U-0647)"
    },
    {
        "college_name": "Sambalpur University Institute of Information Technology (SUIIT) (Id: C-40983)",
        "college_type": "Constituent / University College",
        "district": "Sambalpur",
        "state": "Odisha",
        "university": "Sambalpur University, Sambalpur (Id: U-0362)"
    },
    {
        "college_name": "Allahabad School of Agriculture (Id: C-35394)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "Chitamber School of Humanities & Social Sciences (Id: C-35405)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "Christian School of Health Science (Id: C-35404)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "Gospel & Plough School of Theology (Id: C-35406)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "Grace Zamen School of Education (Id: C-35398)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "Halina School of Home Science (Id: C-35401)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "Jacob School of Biotechnology & Bioengineering (Id: C-35399)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "Joseph School of Business Studies (Id: C-35408)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "School of Basic Science (Id: C-35409)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "School of Film and Mass Communication (Id: C-35407)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "School of Forensic Science (Id: C-35410)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "School of Forestry & Environment (Id: C-35402)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "Shepherd School of Engineering & Technology (Id: C-35396)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "Sudha Lal Womens College (Id: C-35397)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "Sunderasan School of Veterinary Science (Id: C-35403)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "Vaugh School of Agricultural Engineering & Technology (Id: C-35395)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "Warner School of Food & Dairy Technology (Id: C-35400)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "Sam Higginbottom Institute of Agriculture, Technology & Sciences, Allahabad (Id: U-0536)"
    },
    {
        "college_name": "Model college of arts , commerce and science (Id: C-42981)",
        "college_type": "Constituent / University College",
        "district": "Buldana",
        "state": "Maharashtra",
        "university": "Sant Gadge Baba Amravati University, Amravati (Id: U-0324)"
    },
    {
        "college_name": "Aspee College of Home Science & Nutrition (Id: C-34238)",
        "college_type": "Constituent / University College",
        "district": "Banas Kantha",
        "state": "Gujarat",
        "university": "Sardarkrushinagar Dantiwada Agricultural University, Banaskantha (Id: U-0150)"
    },
    {
        "college_name": "College of Agri Business Management (Id: C-34234)",
        "college_type": "Constituent / University College",
        "district": "Banas Kantha",
        "state": "Gujarat",
        "university": "Sardarkrushinagar Dantiwada Agricultural University, Banaskantha (Id: U-0150)"
    },
    {
        "college_name": "College of Basic Science & Huminities (Id: C-34243)",
        "college_type": "Constituent / University College",
        "district": "Banas Kantha",
        "state": "Gujarat",
        "university": "Sardarkrushinagar Dantiwada Agricultural University, Banaskantha (Id: U-0150)"
    },
    {
        "college_name": "College of Horticulture (Id: C-34251)",
        "college_type": "Constituent / University College",
        "district": "Banas Kantha",
        "state": "Gujarat",
        "university": "Sardarkrushinagar Dantiwada Agricultural University, Banaskantha (Id: U-0150)"
    },
    {
        "college_name": "College of Renewable Energy & Environmental Engineering (Id: C-34241)",
        "college_type": "Constituent / University College",
        "district": "Banas Kantha",
        "state": "Gujarat",
        "university": "Sardarkrushinagar Dantiwada Agricultural University, Banaskantha (Id: U-0150)"
    },
    {
        "college_name": "College of Veterinary Science & Animal Husbandary (Id: C-34245)",
        "college_type": "Constituent / University College",
        "district": "Banas Kantha",
        "state": "Gujarat",
        "university": "Sardarkrushinagar Dantiwada Agricultural University, Banaskantha (Id: U-0150)"
    },
    {
        "college_name": "C. P. College of Agriculture (Id: C-34236)",
        "college_type": "Constituent / University College",
        "district": "Banas Kantha",
        "state": "Gujarat",
        "university": "Sardarkrushinagar Dantiwada Agricultural University, Banaskantha (Id: U-0150)"
    },
    {
        "college_name": "Shri G. N. Patel College of Dairy Science and Feed Technology (Id: C-34254)",
        "college_type": "Constituent / University College",
        "district": "Banas Kantha",
        "state": "Gujarat",
        "university": "Sardarkrushinagar Dantiwada Agricultural University, Banaskantha (Id: U-0150)"
    },
    {
        "college_name": "MB Patel College of Education, Vallabh Vidyanagar (Id: C-1170)",
        "college_type": "Constituent / University College",
        "district": "Anand",
        "state": "Gujarat",
        "university": "Sardar Patel University, Vallabh Vidyanagar (Id: U-0148)"
    },
    {
        "college_name": "Saveetha College of Nursing (Id: C-16283)",
        "college_type": "Constituent / University College",
        "district": "Kancheepuram",
        "state": "Tamil Nadu",
        "university": "Saveetha University, Chennai (Id: U-0475)"
    },
    {
        "college_name": "Saveetha College of Physiotheraphy (Id: C-16286)",
        "college_type": "Constituent / University College",
        "district": "Kancheepuram",
        "state": "Tamil Nadu",
        "university": "Saveetha University, Chennai (Id: U-0475)"
    },
    {
        "college_name": "Saveetha Dental College (Id: C-16285)",
        "college_type": "Constituent / University College",
        "district": "Thiruvallur",
        "state": "Tamil Nadu",
        "university": "Saveetha University, Chennai (Id: U-0475)"
    },
    {
        "college_name": "Saveetha Medical College (Id: C-16281)",
        "college_type": "Constituent / University College",
        "district": "Kancheepuram",
        "state": "Tamil Nadu",
        "university": "Saveetha University, Chennai (Id: U-0475)"
    },
    {
        "college_name": "Saveetha School of Engineering (Id: C-16287)",
        "college_type": "Constituent / University College",
        "district": "Kancheepuram",
        "state": "Tamil Nadu",
        "university": "Saveetha University, Chennai (Id: U-0475)"
    },
    {
        "college_name": "Saveetha School of Law (Id: C-16282)",
        "college_type": "Constituent / University College",
        "district": "Thiruvallur",
        "state": "Tamil Nadu",
        "university": "Saveetha University, Chennai (Id: U-0475)"
    },
    {
        "college_name": "Saveetha School of Management (Id: C-16284)",
        "college_type": "Constituent / University College",
        "district": "Thiruvallur",
        "state": "Tamil Nadu",
        "university": "Saveetha University, Chennai (Id: U-0475)"
    },
    {
        "college_name": "Institute of Business & Computer Studies( Faculty of Management Studies) (Id: C-42715)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Shiksha 'O' Anusandhan (Id: U-0363)"
    },
    {
        "college_name": "Institute of Dental Sciences(Faculty of Dental Sciences) (Id: C-42716)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Shiksha 'O' Anusandhan (Id: U-0363)"
    },
    {
        "college_name": "Institute of Medical Sciences and SUM Hospital( Faculty of Medical Sciences) (Id: C-42711)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Shiksha 'O' Anusandhan (Id: U-0363)"
    },
    {
        "college_name": "Institute of Technical Education & Research(Faculty of Engineering and Technology) (Id: C-42709)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Shiksha 'O' Anusandhan (Id: U-0363)"
    },
    {
        "college_name": "School of Hotel Management(Faculty of Hotel Management) (Id: C-42710)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Shiksha 'O' Anusandhan (Id: U-0363)"
    },
    {
        "college_name": "School of Pharmaceutical Sciences(Faculty of Pharmaceutical Sciences) (Id: C-42714)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Shiksha 'O' Anusandhan (Id: U-0363)"
    },
    {
        "college_name": "SOA National Institute of Law (Id: C-42712)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Shiksha 'O' Anusandhan (Id: U-0363)"
    },
    {
        "college_name": "SUM Nursing College(Faculty of Nursing) (Id: C-42713)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Shiksha 'O' Anusandhan (Id: U-0363)"
    },
    {
        "college_name": "Sanskrit College (Id: C-1135)",
        "college_type": "Constituent / University College",
        "district": "Junagadh",
        "state": "Gujarat",
        "university": "Shree Somnath Sanskrit University, Junagarh (Id: U-0152)"
    },
    {
        "college_name": "College of Engineering (Id: C-29466)",
        "college_type": "Constituent / University College",
        "district": "Reasi",
        "state": "Jammu and Kashmir",
        "university": "Shri Mata Vaishno Devi University, Jammu (Id: U-0201)"
    },
    {
        "college_name": "College of Humanities and Social Sciences (Id: C-29464)",
        "college_type": "Constituent / University College",
        "district": "Reasi",
        "state": "Jammu and Kashmir",
        "university": "Shri Mata Vaishno Devi University, Jammu (Id: U-0201)"
    },
    {
        "college_name": "College of Management (Id: C-29467)",
        "college_type": "Constituent / University College",
        "district": "Reasi",
        "state": "Jammu and Kashmir",
        "university": "Shri Mata Vaishno Devi University, Jammu (Id: U-0201)"
    },
    {
        "college_name": "College of Sciences (Id: C-29465)",
        "college_type": "Constituent / University College",
        "district": "Reasi",
        "state": "Jammu and Kashmir",
        "university": "Shri Mata Vaishno Devi University, Jammu (Id: U-0201)"
    },
    {
        "college_name": "J.K.College (Id: C-44713)",
        "college_type": "Constituent / University College",
        "district": "Puruliya",
        "state": "West Bengal",
        "university": "Sidho-Kanho Birsa University (Id: U-0583)"
    },
    {
        "college_name": "Manbhum Mahavidyalaya (Id: C-44642)",
        "college_type": "Constituent / University College",
        "district": "Puruliya",
        "state": "West Bengal",
        "university": "Sidho-Kanho Birsa University (Id: U-0583)"
    },
    {
        "college_name": "A S COLLEGE, DEOGHAR (Id: C-45389)",
        "college_type": "Constituent / University College",
        "district": "Deoghar",
        "state": "Jharkhand",
        "university": "Sido Kanhu Murmu University, Dumka (Id: U-0210)"
    },
    {
        "college_name": "B S K COLLEGE, SAHIBGANJ (Id: C-45399)",
        "college_type": "Constituent / University College",
        "district": "Sahibganj",
        "state": "Jharkhand",
        "university": "Sido Kanhu Murmu University, Dumka (Id: U-0210)"
    },
    {
        "college_name": "DEOGHAR COLLEGE, DEOGHAR (Id: C-45390)",
        "college_type": "Constituent / University College",
        "district": "Deoghar",
        "state": "Jharkhand",
        "university": "Sido Kanhu Murmu University, Dumka (Id: U-0210)"
    },
    {
        "college_name": "GODDA COLLEGE, GODDA (Id: C-45395)",
        "college_type": "Constituent / University College",
        "district": "Godda",
        "state": "Jharkhand",
        "university": "Sido Kanhu Murmu University, Dumka (Id: U-0210)"
    },
    {
        "college_name": "JAMTARA COLLEGE, JAMTARA (Id: C-45397)",
        "college_type": "Constituent / University College",
        "district": "Jamtara",
        "state": "Jharkhand",
        "university": "Sido Kanhu Murmu University, Dumka (Id: U-0210)"
    },
    {
        "college_name": "K K M COLLEGE, PAKUR (Id: C-45398)",
        "college_type": "Constituent / University College",
        "district": "Pakur",
        "state": "Jharkhand",
        "university": "Sido Kanhu Murmu University, Dumka (Id: U-0210)"
    },
    {
        "college_name": "MADHUPUR COLLEGE, DEOGHAR (Id: C-45391)",
        "college_type": "Constituent / University College",
        "district": "Deoghar",
        "state": "Jharkhand",
        "university": "Sido Kanhu Murmu University, Dumka (Id: U-0210)"
    },
    {
        "college_name": "MILLAT COLLEGE, GODDA (Id: C-45396)",
        "college_type": "Constituent / University College",
        "district": "Godda",
        "state": "Jharkhand",
        "university": "Sido Kanhu Murmu University, Dumka (Id: U-0210)"
    },
    {
        "college_name": "R D B MAHILA COLLEGE, DEOGHAR (Id: C-45392)",
        "college_type": "Constituent / University College",
        "district": "Deoghar",
        "state": "Jharkhand",
        "university": "Sido Kanhu Murmu University, Dumka (Id: U-0210)"
    },
    {
        "college_name": "SAHIBGANJ COLLEGE, SAHIBGANJ (Id: C-45401)",
        "college_type": "Constituent / University College",
        "district": "Sahibganj",
        "state": "Jharkhand",
        "university": "Sido Kanhu Murmu University, Dumka (Id: U-0210)"
    },
    {
        "college_name": "S P COLLEGE, DUMKA (Id: C-45393)",
        "college_type": "Constituent / University College",
        "district": "Dumka",
        "state": "Jharkhand",
        "university": "Sido Kanhu Murmu University, Dumka (Id: U-0210)"
    },
    {
        "college_name": "S P MAHILA COLLEGE, DUMKA (Id: C-45394)",
        "college_type": "Constituent / University College",
        "district": "Dumka",
        "state": "Jharkhand",
        "university": "Sido Kanhu Murmu University, Dumka (Id: U-0210)"
    },
    {
        "college_name": "S R T COLLEGE, GODDA (Id: C-45400)",
        "college_type": "Constituent / University College",
        "district": "Godda",
        "state": "Jharkhand",
        "university": "Sido Kanhu Murmu University, Dumka (Id: U-0210)"
    },
    {
        "college_name": "School of Basic & Applied Sciences (SBAS) (Id: C-8628)",
        "college_type": "Constituent / University College",
        "district": "East District",
        "state": "Sikkim",
        "university": "Sikkim Manipal University, Gangtok (Id: U-0431)"
    },
    {
        "college_name": "Sikkim Manipal College of Nursing (SMCON) (Id: C-8624)",
        "college_type": "Constituent / University College",
        "district": "East District",
        "state": "Sikkim",
        "university": "Sikkim Manipal University, Gangtok (Id: U-0431)"
    },
    {
        "college_name": "Sikkim Manipal College of Physiotherapy (SMCOP) (Id: C-8626)",
        "college_type": "Constituent / University College",
        "district": "East District",
        "state": "Sikkim",
        "university": "Sikkim Manipal University, Gangtok (Id: U-0431)"
    },
    {
        "college_name": "Sikkim Manipal Institute of Medical Sciences (SMIMS) (Id: C-8625)",
        "college_type": "Constituent / University College",
        "district": "East District",
        "state": "Sikkim",
        "university": "Sikkim Manipal University, Gangtok (Id: U-0431)"
    },
    {
        "college_name": "Sikkim Manipal Institute of Technology (SMIT) (Id: C-8627)",
        "college_type": "Constituent / University College",
        "district": "East District",
        "state": "Sikkim",
        "university": "Sikkim Manipal University, Gangtok (Id: U-0431)"
    },
    {
        "college_name": "C.U.Shah College of Pharmacy (Id: C-44200)",
        "college_type": "Constituent / University College",
        "district": "Mumbai",
        "state": "Maharashtra",
        "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
    },
    {
        "college_name": "Jankidevi Bajaj Institute of Management Studies (Id: C-44326)",
        "college_type": "Constituent / University College",
        "district": "Mumbai",
        "state": "Maharashtra",
        "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
    },
    {
        "college_name": "Leelabai Thackersey College of Nursing (Id: C-44151)",
        "college_type": "Constituent / University College",
        "district": "Mumbai",
        "state": "Maharashtra",
        "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
    },
    {
        "college_name": "Prmlila Vithalda Polytechnic (Id: C-44267)",
        "college_type": "Constituent / University College",
        "district": "Mumbai",
        "state": "Maharashtra",
        "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
    },
    {
        "college_name": "P.V.D.T. College of Education for Women (Id: C-44220)",
        "college_type": "Constituent / University College",
        "district": "Mumbai",
        "state": "Maharashtra",
        "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
    },
    {
        "college_name": "S.H.P.T. College of Science (Id: C-44266)",
        "college_type": "Constituent / University College",
        "district": "Mumbai",
        "state": "Maharashtra",
        "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
    },
    {
        "college_name": "SHPT School of Library Science (Id: C-44196)",
        "college_type": "Constituent / University College",
        "district": "Mumbai",
        "state": "Maharashtra",
        "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
    },
    {
        "college_name": "S.N.D.T. Arts & Commerce College for Women (Id: C-44250)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
    },
    {
        "college_name": "S.N.D.T. College of Arts and Smt. C.B. College of Commerce and Science for Women (Id: C-44176)",
        "college_type": "Constituent / University College",
        "district": "Mumbai",
        "state": "Maharashtra",
        "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
    },
    {
        "college_name": "S.N.D.T. College of Education for Women (Id: C-44322)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
    },
    {
        "college_name": "S.N.D.T. College of Home Science (Id: C-44118)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
    },
    {
        "college_name": "S.V.T. College of Home Science (Autonomous College) (Id: C-44265)",
        "college_type": "Constituent / University College",
        "district": "Mumbai",
        "state": "Maharashtra",
        "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
    },
    {
        "college_name": "Usha Mittal Institute of Technology for Women (Id: C-44230)",
        "college_type": "Constituent / University College",
        "district": "Mumbai",
        "state": "Maharashtra",
        "university": "Smt. Nathibai Damodar Thackersey Women's Univeristy, Mumbai (Id: U-0326)"
    },
    {
        "college_name": "INDIRA GANDHI INSTITUTE OF DENTAL SCIENCES (Id: C-47764)",
        "college_type": "Constituent / University College",
        "district": "Puducherry",
        "state": "Puducherry",
        "university": "Sri Balajai Vidyapeeth Mahatma Gandhi Medical College, Puducherry (Id: U-0370)"
    },
    {
        "college_name": "KASTURBA GANDHI NURSING COLLEGE (Id: C-47763)",
        "college_type": "Constituent / University College",
        "district": "Puducherry",
        "state": "Puducherry",
        "university": "Sri Balajai Vidyapeeth Mahatma Gandhi Medical College, Puducherry (Id: U-0370)"
    },
    {
        "college_name": "MAHATMA GANDHI MEDICAL COLLEGE AND RESEARCH INSTITUTE (Id: C-47762)",
        "college_type": "Constituent / University College",
        "district": "Puducherry",
        "state": "Puducherry",
        "university": "Sri Balajai Vidyapeeth Mahatma Gandhi Medical College, Puducherry (Id: U-0370)"
    },
    {
        "college_name": "SHRI SATHYA SAI MEDICAL COLLEGE AND RESEARCH INSTITUTE (Id: C-47765)",
        "college_type": "Constituent / University College",
        "district": "Kancheepuram",
        "state": "Tamil Nadu",
        "university": "Sri Balajai Vidyapeeth Mahatma Gandhi Medical College, Puducherry (Id: U-0370)"
    },
    {
        "college_name": "Sri Devaraj Urs Medical College (Id: C-15585)",
        "college_type": "Constituent / University College",
        "district": "Kolar",
        "state": "Karnataka",
        "university": "Sri Devraj Urs Acaedmy of Highehr Education and Research, Kolar (Id: U-0241)"
    },
    {
        "college_name": "SKU College (Id: C-30968)",
        "college_type": "Constituent / University College",
        "district": "Anantapur",
        "state": "Andhra Pradesh",
        "university": "Sri Krishnadevaraya University, Anantapur (Id: U-0033)"
    },
    {
        "college_name": "SKU College of Education (Id: C-30928)",
        "college_type": "Constituent / University College",
        "district": "Anantapur",
        "state": "Andhra Pradesh",
        "university": "Sri Krishnadevaraya University, Anantapur (Id: U-0033)"
    },
    {
        "college_name": "SKU College of Engineering & Technology (Id: C-31019)",
        "college_type": "Constituent / University College",
        "district": "Anantapur",
        "state": "Andhra Pradesh",
        "university": "Sri Krishnadevaraya University, Anantapur (Id: U-0033)"
    },
    {
        "college_name": "SKU College of Pharmacy (Id: C-30998)",
        "college_type": "Constituent / University College",
        "district": "Anantapur",
        "state": "Andhra Pradesh",
        "university": "Sri Krishnadevaraya University, Anantapur (Id: U-0033)"
    },
    {
        "college_name": "Sri Ramachandra College of Allied Health Sciences (Id: C-35712)",
        "college_type": "Constituent / University College",
        "district": "Thiruvallur",
        "state": "Tamil Nadu",
        "university": "Sri Ramachandra Medical College and Research Institute, Chennai (Id: U-0478)"
    },
    {
        "college_name": "Sri Ramachandra College of Biomedical Sciences, Technology & Research (Id: C-35714)",
        "college_type": "Constituent / University College",
        "district": "Thiruvallur",
        "state": "Tamil Nadu",
        "university": "Sri Ramachandra Medical College and Research Institute, Chennai (Id: U-0478)"
    },
    {
        "college_name": "Sri Ramachandra College of Management (Id: C-35710)",
        "college_type": "Constituent / University College",
        "district": "Thiruvallur",
        "state": "Tamil Nadu",
        "university": "Sri Ramachandra Medical College and Research Institute, Chennai (Id: U-0478)"
    },
    {
        "college_name": "Sri Ramachandra College of Nursing (Id: C-35708)",
        "college_type": "Constituent / University College",
        "district": "Thiruvallur",
        "state": "Tamil Nadu",
        "university": "Sri Ramachandra Medical College and Research Institute, Chennai (Id: U-0478)"
    },
    {
        "college_name": "Sri Ramachandra College of Pharmacy (Id: C-35709)",
        "college_type": "Constituent / University College",
        "district": "Thiruvallur",
        "state": "Tamil Nadu",
        "university": "Sri Ramachandra Medical College and Research Institute, Chennai (Id: U-0478)"
    },
    {
        "college_name": "Sri Ramachandra College of Physiotherapy (Id: C-35713)",
        "college_type": "Constituent / University College",
        "district": "Thiruvallur",
        "state": "Tamil Nadu",
        "university": "Sri Ramachandra Medical College and Research Institute, Chennai (Id: U-0478)"
    },
    {
        "college_name": "Sri Ramachandra Dental College & Hospital (Id: C-35711)",
        "college_type": "Constituent / University College",
        "district": "Thiruvallur",
        "state": "Tamil Nadu",
        "university": "Sri Ramachandra Medical College and Research Institute, Chennai (Id: U-0478)"
    },
    {
        "college_name": "Sri Ramachandra Medical College and Research Institute (Id: C-35707)",
        "college_type": "Constituent / University College",
        "district": "Thiruvallur",
        "state": "Tamil Nadu",
        "university": "Sri Ramachandra Medical College and Research Institute, Chennai (Id: U-0478)"
    },
    {
        "college_name": "Anantapur Campus (Off-Campus centre) for women at Anantapur, Anantapur District, Andhra Pradesh (Id: C-29451)",
        "college_type": "Constituent / University College",
        "district": "Anantapur",
        "state": "Andhra Pradesh",
        "university": "Sri Satya Sai Institute of Higher Learning, Anantpur (Id: U-0035)"
    },
    {
        "college_name": "Brindavan Campus (Off-Campus centre) for men at Kadugodi, Whitefield, Bangalore, Karnataka (Id: C-29452)",
        "college_type": "Constituent / University College",
        "district": "Bangalore Rural",
        "state": "Karnataka",
        "university": "Sri Satya Sai Institute of Higher Learning, Anantpur (Id: U-0035)"
    },
    {
        "college_name": "Prasanthi Nilayam Campus (Main) for men at Prasanthi Nilayam, Anantapur District, Andhra Pradesh (Id: C-29450)",
        "college_type": "Constituent / University College",
        "district": "Anantapur",
        "state": "Andhra Pradesh",
        "university": "Sri Satya Sai Institute of Higher Learning, Anantpur (Id: U-0035)"
    },
    {
        "college_name": "Sri Siddhartha Dental college, Tumkur (Id: C-36485)",
        "college_type": "Constituent / University College",
        "district": "Tumkur",
        "state": "Karnataka",
        "university": "Sri Siddharatha Acedemy of Higher Education (Id: U-0242)"
    },
    {
        "college_name": "Sri Siddhartha Institute of Technology, Tumkur. (Id: C-36483)",
        "college_type": "Constituent / University College",
        "district": "Tumkur",
        "state": "Karnataka",
        "university": "Sri Siddharatha Acedemy of Higher Education (Id: U-0242)"
    },
    {
        "college_name": "Sri Siddhartha Medical College, Tumkur (Id: C-36484)",
        "college_type": "Constituent / University College",
        "district": "Tumkur",
        "state": "Karnataka",
        "university": "Sri Siddharatha Acedemy of Higher Education (Id: U-0242)"
    },
    {
        "college_name": "College of Nursing (Id: C-16167)",
        "college_type": "Constituent / University College",
        "district": "Chittoor",
        "state": "Andhra Pradesh",
        "university": "Sri Venkateswara Institute of Medical Sciences, Tirupathi (Id: U-0036)"
    },
    {
        "college_name": "College of Physiotherapy (Id: C-16166)",
        "college_type": "Constituent / University College",
        "district": "Chittoor",
        "state": "Andhra Pradesh",
        "university": "Sri Venkateswara Institute of Medical Sciences, Tirupathi (Id: U-0036)"
    },
    {
        "college_name": "S.V.U. College of Arts, Tirupati (Id: C-27636)",
        "college_type": "Constituent / University College",
        "district": "Chittoor",
        "state": "Andhra Pradesh",
        "university": "Sri Venkateswara University, Tirupathy (Id: U-0037)"
    },
    {
        "college_name": "S.V.U. College of Commerce, Management & Information Sciences, Tirupati (Id: C-27769)",
        "college_type": "Constituent / University College",
        "district": "Chittoor",
        "state": "Andhra Pradesh",
        "university": "Sri Venkateswara University, Tirupathy (Id: U-0037)"
    },
    {
        "college_name": "S.V.U. College of Engineering, Tirupati (Id: C-27675)",
        "college_type": "Constituent / University College",
        "district": "Chittoor",
        "state": "Andhra Pradesh",
        "university": "Sri Venkateswara University, Tirupathy (Id: U-0037)"
    },
    {
        "college_name": "S.V.U. College of Sciences, Tirupati (Id: C-27712)",
        "college_type": "Constituent / University College",
        "district": "Chittoor",
        "state": "Andhra Pradesh",
        "university": "Sri Venkateswara University, Tirupathy (Id: U-0037)"
    },
    {
        "college_name": "College of Dairy Technology, Tirupati (Id: C-22049)",
        "college_type": "Constituent / University College",
        "district": "Chittoor",
        "state": "Andhra Pradesh",
        "university": "Sri Venkateswara Veterinary University, Tirupathi (Id: U-0039)"
    },
    {
        "college_name": "College of Fishery Science, Muthukur (Id: C-22048)",
        "college_type": "Constituent / University College",
        "district": "Sri Potti Sriramulu Nellore",
        "state": "Andhra Pradesh",
        "university": "Sri Venkateswara Veterinary University, Tirupathi (Id: U-0039)"
    },
    {
        "college_name": "College of Veterinary Science, Korutla (Id: C-29256)",
        "college_type": "Constituent / University College",
        "district": "Karimnagar",
        "state": "Telangana",
        "university": "Sri Venkateswara Veterinary University, Tirupathi (Id: U-0039)"
    },
    {
        "college_name": "College of Veterinary Science, Proddutur (Id: C-22052)",
        "college_type": "Constituent / University College",
        "district": "Y.S.R.",
        "state": "Andhra Pradesh",
        "university": "Sri Venkateswara Veterinary University, Tirupathi (Id: U-0039)"
    },
    {
        "college_name": "College of Veterinary Science, Rajendranagar, Hyderabad (Id: C-22047)",
        "college_type": "Constituent / University College",
        "district": "Rangareddy",
        "state": "Telangana",
        "university": "Sri Venkateswara Veterinary University, Tirupathi (Id: U-0039)"
    },
    {
        "college_name": "College of Veterinary Science, Tirupati (Id: C-22051)",
        "college_type": "Constituent / University College",
        "district": "Chittoor",
        "state": "Andhra Pradesh",
        "university": "Sri Venkateswara Veterinary University, Tirupathi (Id: U-0039)"
    },
    {
        "college_name": "Dairy Technology Programme, Kamareddy (Id: C-22054)",
        "college_type": "Constituent / University College",
        "district": "Nizamabad",
        "state": "Telangana",
        "university": "Sri Venkateswara Veterinary University, Tirupathi (Id: U-0039)"
    },
    {
        "college_name": "NTR College of Veterinary Science, Gannavaram (Id: C-22050)",
        "college_type": "Constituent / University College",
        "district": "Krishna",
        "state": "Andhra Pradesh",
        "university": "Sri Venkateswara Veterinary University, Tirupathi (Id: U-0039)"
    },
    {
        "college_name": "College of Physiotherapy (Id: C-1099)",
        "college_type": "Constituent / University College",
        "district": "Vadodara",
        "state": "Gujarat",
        "university": "Sumandeep Vidyappeth, Vadodara (Id: U-0154)"
    },
    {
        "college_name": "K.M shah dental college & Hospital (Id: C-1101)",
        "college_type": "Constituent / University College",
        "district": "Vadodara",
        "state": "Gujarat",
        "university": "Sumandeep Vidyappeth, Vadodara (Id: U-0154)"
    },
    {
        "college_name": "Smt. B.K Shah Medical College & Research centre (Id: C-1102)",
        "college_type": "Constituent / University College",
        "district": "Vadodara",
        "state": "Gujarat",
        "university": "Sumandeep Vidyappeth, Vadodara (Id: U-0154)"
    },
    {
        "college_name": "Sumandeep Nursing College (Id: C-1100)",
        "college_type": "Constituent / University College",
        "district": "Vadodara",
        "state": "Gujarat",
        "university": "Sumandeep Vidyappeth, Vadodara (Id: U-0154)"
    },
    {
        "college_name": "Gyan Vihar International School of Business Management (Id: C-44866)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "Suresh Gyan Vihar Univeristy, Jaipur (Id: U-0427)"
    },
    {
        "college_name": "Gyan Vihar School of Engineering & Technology (Id: C-44868)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "Suresh Gyan Vihar Univeristy, Jaipur (Id: U-0427)"
    },
    {
        "college_name": "Gyan Vihar School of Hotel Management (Id: C-44865)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "Suresh Gyan Vihar Univeristy, Jaipur (Id: U-0427)"
    },
    {
        "college_name": "Gyan Vihar School of Sciences (Id: C-44869)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "Suresh Gyan Vihar Univeristy, Jaipur (Id: U-0427)"
    },
    {
        "college_name": "Gyan Vihar Shcool of Pharmacy (Id: C-44867)",
        "college_type": "Constituent / University College",
        "district": "Jaipur",
        "state": "Rajasthan",
        "university": "Suresh Gyan Vihar Univeristy, Jaipur (Id: U-0427)"
    },
    {
        "college_name": "NEW MODEL DEGREE COLLEGE, HINGOLI (Id: C-45274)",
        "college_type": "Constituent / University College",
        "district": "Hingoli",
        "state": "Maharashtra",
        "university": "Swami Ramanand Teerth Marathwada University, Nanded (Id: U-0328)"
    },
    {
        "college_name": "English Language Teaching Institute of Symbiosis & SIFIL (Id: C-19346)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Centre for Information Technology (Id: C-19330)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Centre for Management and Human Resource Development (Id: C-19339)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Centre for Management Studies, Pune (SCMS-Pune). (Id: C-19325)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis College of Nursing (Id: C-19345)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Institute of Business Management, Pune (Id: C-19343)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Institute of Computer Studies and Research (Id: C-19331)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Institute of Design (Id: C-19350)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Institute of Geoinformatics (Id: C-19337)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Institute of Health Sciences (Id: C-19338)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Institute of International Business (Id: C-19332)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Institute of Management Studies (Id: C-19349)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Institute of Media & Communication, Pune (Id: C-19340)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Institute of Media & Communication, UG (Id: C-19347)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Institute of Operations Management (Id: C-19348)",
        "college_type": "Constituent / University College",
        "district": "Nashik",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Institute of Technology (Id: C-19344)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Institute of Telecom Management (Id: C-19329)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis Law School, Pune (Id: C-19328)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis School for Liberal Arts (Id: C-45067)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis School of Banking Management (Id: C-19341)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis School of Biomedical Sciences (Id: C-45069)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis School of Economics (Id: C-19342)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Symbiosis School of Photography (Id: C-45068)",
        "college_type": "Constituent / University College",
        "district": "Pune",
        "state": "Maharashtra",
        "university": "SYMBIOSIS International University, Pune (Id: U-0329)"
    },
    {
        "college_name": "Agricultural College and Research Institute, Coimbatore (Id: C-44926)",
        "college_type": "Constituent / University College",
        "district": "Coimbatore",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Agricultural University, Coimbatore (Id: U-0485)"
    },
    {
        "college_name": "Agricultural College and Research Institute, Madurai (Id: C-44925)",
        "college_type": "Constituent / University College",
        "district": "Madurai",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Agricultural University, Coimbatore (Id: U-0485)"
    },
    {
        "college_name": "Agricultural College and Research Institute, Thoothukkudi (Id: C-44918)",
        "college_type": "Constituent / University College",
        "district": "Thoothukkudi",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Agricultural University, Coimbatore (Id: U-0485)"
    },
    {
        "college_name": "Agricultural Engineering College and Research Institute, Coimbatore (Id: C-44924)",
        "college_type": "Constituent / University College",
        "district": "Coimbatore",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Agricultural University, Coimbatore (Id: U-0485)"
    },
    {
        "college_name": "Agricultural Engineering College and Research Institute, Tiruchirappalli (Id: C-44929)",
        "college_type": "Constituent / University College",
        "district": "Tiruchirappalli",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Agricultural University, Coimbatore (Id: U-0485)"
    },
    {
        "college_name": "Anbil Dharmalingam Agricultural College and Research Institute (Id: C-44927)",
        "college_type": "Constituent / University College",
        "district": "Tiruchirappalli",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Agricultural University, Coimbatore (Id: U-0485)"
    },
    {
        "college_name": "Forest College and Research Institute (Id: C-44920)",
        "college_type": "Constituent / University College",
        "district": "Coimbatore",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Agricultural University, Coimbatore (Id: U-0485)"
    },
    {
        "college_name": "Home Science College and Research Institute (Id: C-44921)",
        "college_type": "Constituent / University College",
        "district": "Madurai",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Agricultural University, Coimbatore (Id: U-0485)"
    },
    {
        "college_name": "Horticultural College and Research Institute, Coimbatore (Id: C-44923)",
        "college_type": "Constituent / University College",
        "district": "Coimbatore",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Agricultural University, Coimbatore (Id: U-0485)"
    },
    {
        "college_name": "Horticultural College and Research Institute for Women (Id: C-44928)",
        "college_type": "Constituent / University College",
        "district": "Tiruchirappalli",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Agricultural University, Coimbatore (Id: U-0485)"
    },
    {
        "college_name": "Horticultural College and Research Institute, Theni (Id: C-44922)",
        "college_type": "Constituent / University College",
        "district": "Theni",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Agricultural University, Coimbatore (Id: U-0485)"
    },
    {
        "college_name": "Fisheries College and Research Institute, Thoothukudi (Id: C-42738)",
        "college_type": "Constituent / University College",
        "district": "Thoothukkudi",
        "state": "Tamil Nadu",
        "university": "TAMIL NADU FISHERIES UNIVERSITY (Id: U-0665)"
    },
    {
        "college_name": "College of Food and Dairy Technology, Koduvalli (Id: C-42740)",
        "college_type": "Constituent / University College",
        "district": "Thiruvallur",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Veterinary & Animal Sciences University, Chennai (Id: U-0487)"
    },
    {
        "college_name": "College of Poultry Production and Management, Hosur (Id: C-48239)",
        "college_type": "Constituent / University College",
        "district": "Krishnagiri",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Veterinary & Animal Sciences University, Chennai (Id: U-0487)"
    },
    {
        "college_name": "Madras Veterinary College, Chennai - 7 (Id: C-42741)",
        "college_type": "Constituent / University College",
        "district": "Chennai",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Veterinary & Animal Sciences University, Chennai (Id: U-0487)"
    },
    {
        "college_name": "Post Graduate Research Institute in Animal Sciences, Kattupakkam (Id: C-45930)",
        "college_type": "Constituent / University College",
        "district": "Kancheepuram",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Veterinary & Animal Sciences University, Chennai (Id: U-0487)"
    },
    {
        "college_name": "Veterinary College and Research Institute, Namakkal (Id: C-42739)",
        "college_type": "Constituent / University College",
        "district": "Namakkal",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Veterinary & Animal Sciences University, Chennai (Id: U-0487)"
    },
    {
        "college_name": "Veterinary College and Research Institute, Orathanad (Id: C-47826)",
        "college_type": "Constituent / University College",
        "district": "Thanjavur",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Veterinary & Animal Sciences University, Chennai (Id: U-0487)"
    },
    {
        "college_name": "Veterinary College and Research Institute, Tirunelveli (Id: C-47827)",
        "college_type": "Constituent / University College",
        "district": "Tirunelveli",
        "state": "Tamil Nadu",
        "university": "Tamilnadu Veterinary & Animal Sciences University, Chennai (Id: U-0487)"
    },
    {
        "college_name": "Teerthanker Mahaveer College of Engineering (Id: C-42729)",
        "college_type": "Constituent / University College",
        "district": "Moradabad",
        "state": "Uttar Pradesh",
        "university": "Teerthanker Mahaveer University, Moradabad (Id: U-0544)"
    },
    {
        "college_name": "Teerthanker Mahaveer College of Law and Legal Studies (Id: C-42728)",
        "college_type": "Constituent / University College",
        "district": "Moradabad",
        "state": "Uttar Pradesh",
        "university": "Teerthanker Mahaveer University, Moradabad (Id: U-0544)"
    },
    {
        "college_name": "Teerthanker Mahaveer College of Management and Computer Applications (Id: C-42732)",
        "college_type": "Constituent / University College",
        "district": "Moradabad",
        "state": "Uttar Pradesh",
        "university": "Teerthanker Mahaveer University, Moradabad (Id: U-0544)"
    },
    {
        "college_name": "Teerthanker Mahaveer College of Nursing (Id: C-42727)",
        "college_type": "Constituent / University College",
        "district": "Moradabad",
        "state": "Uttar Pradesh",
        "university": "Teerthanker Mahaveer University, Moradabad (Id: U-0544)"
    },
    {
        "college_name": "Teerthanker Mahaveer College of Paramedical Sciences (Id: C-42731)",
        "college_type": "Constituent / University College",
        "district": "Moradabad",
        "state": "Uttar Pradesh",
        "university": "Teerthanker Mahaveer University, Moradabad (Id: U-0544)"
    },
    {
        "college_name": "Teerthanker Mahaveer College of Pharmacy (Id: C-42722)",
        "college_type": "Constituent / University College",
        "district": "Moradabad",
        "state": "Uttar Pradesh",
        "university": "Teerthanker Mahaveer University, Moradabad (Id: U-0544)"
    },
    {
        "college_name": "Teerthanker Mahaveer Dental College and Research Centre (Id: C-42723)",
        "college_type": "Constituent / University College",
        "district": "Moradabad",
        "state": "Uttar Pradesh",
        "university": "Teerthanker Mahaveer University, Moradabad (Id: U-0544)"
    },
    {
        "college_name": "Teerthanker Mahaveer Medical College & Research Centre (Id: C-42724)",
        "college_type": "Constituent / University College",
        "district": "Moradabad",
        "state": "Uttar Pradesh",
        "university": "Teerthanker Mahaveer University, Moradabad (Id: U-0544)"
    },
    {
        "college_name": "Teerthanker Mahaveer of College of Architecture (Id: C-42730)",
        "college_type": "Constituent / University College",
        "district": "Moradabad",
        "state": "Uttar Pradesh",
        "university": "Teerthanker Mahaveer University, Moradabad (Id: U-0544)"
    },
    {
        "college_name": "Teerthanker Mahaveer of College of Education (Id: C-42725)",
        "college_type": "Constituent / University College",
        "district": "Moradabad",
        "state": "Uttar Pradesh",
        "university": "Teerthanker Mahaveer University, Moradabad (Id: U-0544)"
    },
    {
        "college_name": "Teerthanker Mahaveer Polytechnic (Id: C-42726)",
        "college_type": "Constituent / University College",
        "district": "Moradabad",
        "state": "Uttar Pradesh",
        "university": "Teerthanker Mahaveer University, Moradabad (Id: U-0544)"
    },
    {
        "college_name": "FACULTY OF EDUCATION (Id: C-35078)",
        "college_type": "Constituent / University College",
        "district": "West Tripura",
        "state": "Tripura",
        "university": "The Institute of Chartered Financial Analysts of India University, Agartala (Id: U-0494)"
    },
    {
        "college_name": "FACULTY OF LAW (Id: C-35077)",
        "college_type": "Constituent / University College",
        "district": "West Tripura",
        "state": "Tripura",
        "university": "The Institute of Chartered Financial Analysts of India University, Agartala (Id: U-0494)"
    },
    {
        "college_name": "FACULTY OF MANAGEMENT STUDIES (Id: C-35079)",
        "college_type": "Constituent / University College",
        "district": "West Tripura",
        "state": "Tripura",
        "university": "The Institute of Chartered Financial Analysts of India University, Agartala (Id: U-0494)"
    },
    {
        "college_name": "FACULTY OF SCIENCE & TECHNOLOGY (Id: C-35080)",
        "college_type": "Constituent / University College",
        "district": "West Tripura",
        "state": "Tripura",
        "university": "The Institute of Chartered Financial Analysts of India University, Agartala (Id: U-0494)"
    },
    {
        "college_name": "College of Medicine and J N M Hospital, Kalyani (Id: C-16382)",
        "college_type": "Constituent / University College",
        "district": "Nadia",
        "state": "West Bengal",
        "university": "The West Bengal University of Health Sciences, Kolkata (Id: U-0586)"
    },
    {
        "college_name": "Thiruvalluvar University college of Arts &Science ,E.V.N.Govt.Boys Higher SEcondary School,Krishanagiri Road,Gazhanayeganpatti,Tirupattur Taluk,Tirupattur-635 901aGd, (Id: C-36420)",
        "college_type": "Constituent / University College",
        "district": "Vellore",
        "state": "Tamil Nadu",
        "university": "Thiruvalluvar Univeristy, Vellore (Id: U-0488)"
    },
    {
        "college_name": "Thiruvalluvar University College of Arts &SCience,Panchayat Union Middle School,Kacharapalayam Road, Kallakuruchi-606 202 (Id: C-36351)",
        "college_type": "Constituent / University College",
        "district": "Viluppuram",
        "state": "Tamil Nadu",
        "university": "Thiruvalluvar Univeristy, Vellore (Id: U-0488)"
    },
    {
        "college_name": "Thiruvalluvar University College of Arts & Science ,Thennangur Village,Vandavasi Taluk-604 408 (Id: C-36364)",
        "college_type": "Constituent / University College",
        "district": "Tiruvannamalai",
        "state": "Tamil Nadu",
        "university": "Thiruvalluvar Univeristy, Vellore (Id: U-0488)"
    },
    {
        "college_name": "Thiruvalluvar University College of Arts &Science,Thiruvannainallur,Tirukoilur-607 203 (Id: C-36380)",
        "college_type": "Constituent / University College",
        "district": "Viluppuram",
        "state": "Tamil Nadu",
        "university": "Thiruvalluvar Univeristy, Vellore (Id: U-0488)"
    },
    {
        "college_name": "B.N. College, Bhagalpur (Id: C-17619)",
        "college_type": "Constituent / University College",
        "district": "Bhagalpur",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "BNM College, Barhaiya (Id: C-17660)",
        "college_type": "Constituent / University College",
        "district": "Lakhisarai",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "BRM College, Munger (Id: C-17640)",
        "college_type": "Constituent / University College",
        "district": "Munger",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "DSM College, Jhajha (Id: C-17624)",
        "college_type": "Constituent / University College",
        "district": "Jamui",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "GB College, Naugachia (Id: C-17649)",
        "college_type": "Constituent / University College",
        "district": "Bhagalpur",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "HS College, Haweli Kharagpur (Id: C-17655)",
        "college_type": "Constituent / University College",
        "district": "Munger",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "Jamalpur College, Jamalpur (Id: C-17630)",
        "college_type": "Constituent / University College",
        "district": "Munger",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "JMS College, Munger (Id: C-17644)",
        "college_type": "Constituent / University College",
        "district": "Munger",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "JP College, Narayanpur (Id: C-17635)",
        "college_type": "Constituent / University College",
        "district": "Bhagalpur",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "JRS College, Jamalpur (Id: C-17628)",
        "college_type": "Constituent / University College",
        "district": "Munger",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "KDS College, Gogri (Id: C-17663)",
        "college_type": "Constituent / University College",
        "district": "Khagaria",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "KKM College, Jamui (Id: C-17636)",
        "college_type": "Constituent / University College",
        "district": "Jamui",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "KMD College, Parbatta (Id: C-17656)",
        "college_type": "Constituent / University College",
        "district": "Khagaria",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "Koshi College, Khagaria (Id: C-17643)",
        "college_type": "Constituent / University College",
        "district": "Khagaria",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "KSS College, Lakhisarai (Id: C-17646)",
        "college_type": "Constituent / University College",
        "district": "Lakhisarai",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "Mahila College, Khagaria (Id: C-17658)",
        "college_type": "Constituent / University College",
        "district": "Khagaria",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "MAM College, Naugachia (Id: C-17651)",
        "college_type": "Constituent / University College",
        "district": "Bhagalpur",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "Marwari College, Bhagalpur (Id: C-17620)",
        "college_type": "Constituent / University College",
        "district": "Bhagalpur",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "Murarka College, Sultanganj (Id: C-17645)",
        "college_type": "Constituent / University College",
        "district": "Bhagalpur",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "PBS College, Banka (Id: C-17629)",
        "college_type": "Constituent / University College",
        "district": "Banka",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "RD College. Sheikhpura (Id: C-17627)",
        "college_type": "Constituent / University College",
        "district": "Sheikhpura",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "RD & DJ College, Munger (Id: C-17662)",
        "college_type": "Constituent / University College",
        "district": "Munger",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "RS College, Tarapur (Id: C-17617)",
        "college_type": "Constituent / University College",
        "district": "Munger",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "Sabour College, Sabour (Id: C-17641)",
        "college_type": "Constituent / University College",
        "district": "Bhagalpur",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "SKR College, Barbigha (Id: C-17637)",
        "college_type": "Constituent / University College",
        "district": "Sheikhpura",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "S.M. College, Bhagalpur (Id: C-17650)",
        "college_type": "Constituent / University College",
        "district": "Bhagalpur",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "SSV College, Kahalgaon (Id: C-17623)",
        "college_type": "Constituent / University College",
        "district": "Bhagalpur",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "T.N.B. College, Bhagalpur (Id: C-17621)",
        "college_type": "Constituent / University College",
        "district": "Bhagalpur",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "TNB Law College, Bhagalpur (Id: C-17648)",
        "college_type": "Constituent / University College",
        "district": "Bhagalpur",
        "state": "Bihar",
        "university": "T.M. Bhagalpur University, Bhagalpur (Id: U-0076)"
    },
    {
        "college_name": "University College of Arts (Id: C-6922)",
        "college_type": "Constituent / University College",
        "district": "Tumkur",
        "state": "Karnataka",
        "university": "Tumkur University, Tumkur (Id: U-0244)"
    },
    {
        "college_name": "University College of Science (Id: C-6943)",
        "college_type": "Constituent / University College",
        "district": "Tumkur",
        "state": "Karnataka",
        "university": "Tumkur University, Tumkur (Id: U-0244)"
    },
    {
        "college_name": "Bhulabhai Vanmalibhai Patel Institute of Business Management, Computer & Information Technology (Id: C-486)",
        "college_type": "Constituent / University College",
        "district": "Surat",
        "state": "Gujarat",
        "university": "UKA TARSADIA UNIVERSITY (Id: U-0668)"
    },
    {
        "college_name": "C G Bhakta Institute of Biotechnology (Id: C-17871)",
        "college_type": "Constituent / University College",
        "district": "Tapi",
        "state": "Gujarat",
        "university": "UKA TARSADIA UNIVERSITY (Id: U-0668)"
    },
    {
        "college_name": "CHHOTUBHAI GOPALBHAI PATEL INSTITUTE OF TECHNOLOGY (Id: C-185)",
        "college_type": "Constituent / University College",
        "district": "Surat",
        "state": "Gujarat",
        "university": "UKA TARSADIA UNIVERSITY (Id: U-0668)"
    },
    {
        "college_name": "MALIBA PHARMACY COLLEGE (Id: C-373)",
        "college_type": "Constituent / University College",
        "district": "Surat",
        "state": "Gujarat",
        "university": "UKA TARSADIA UNIVERSITY (Id: U-0668)"
    },
    {
        "college_name": "Maniba Bhula Nursing College (Id: C-688)",
        "college_type": "Constituent / University College",
        "district": "Surat",
        "state": "Gujarat",
        "university": "UKA TARSADIA UNIVERSITY (Id: U-0668)"
    },
    {
        "college_name": "SHRIMAD RAJCHANDRA COLLEGE OF PHYSIOTHERAPY (Id: C-48372)",
        "college_type": "Constituent / University College",
        "district": "Surat",
        "state": "Gujarat",
        "university": "UKA TARSADIA UNIVERSITY (Id: U-0668)"
    },
    {
        "college_name": "Shrimad Rajchandra Institute of Management and Computer Application (Id: C-345)",
        "college_type": "Constituent / University College",
        "district": "Surat",
        "state": "Gujarat",
        "university": "UKA TARSADIA UNIVERSITY (Id: U-0668)"
    },
    {
        "college_name": "Srimad Rajchandra School of Sports (Id: C-709)",
        "college_type": "Constituent / University College",
        "district": "Surat",
        "state": "Gujarat",
        "university": "UKA TARSADIA UNIVERSITY (Id: U-0668)"
    },
    {
        "college_name": "Agriculture College, Navile,Shimoga (Id: C-36460)",
        "college_type": "Constituent / University College",
        "district": "Shimoga",
        "state": "Karnataka",
        "university": "UNIVERSITY OF AGRICULTURAL AND HORTICULTURAL SCIENCES, SHIMOGA (Id: U-0637)"
    },
    {
        "college_name": "College of Horticulture, Hiriyur (Id: C-35756)",
        "college_type": "Constituent / University College",
        "district": "Chitradurga",
        "state": "Karnataka",
        "university": "UNIVERSITY OF AGRICULTURAL AND HORTICULTURAL SCIENCES, SHIMOGA (Id: U-0637)"
    },
    {
        "college_name": "College of Horticulture, Mudigere (Id: C-35758)",
        "college_type": "Constituent / University College",
        "district": "Chikmagalur",
        "state": "Karnataka",
        "university": "UNIVERSITY OF AGRICULTURAL AND HORTICULTURAL SCIENCES, SHIMOGA (Id: U-0637)"
    },
    {
        "college_name": "Forestry College, Ponnampet (Id: C-36461)",
        "college_type": "Constituent / University College",
        "district": "Kodagu",
        "state": "Karnataka",
        "university": "UNIVERSITY OF AGRICULTURAL AND HORTICULTURAL SCIENCES, SHIMOGA (Id: U-0637)"
    },
    {
        "college_name": "Agriculture College, GKVK,Bangalore (Id: C-36456)",
        "college_type": "Constituent / University College",
        "district": "Bangalore",
        "state": "Karnataka",
        "university": "University of Agricultural Sciences, Bangalore (Id: U-0248)"
    },
    {
        "college_name": "Agriculture College, Hassan (Id: C-36457)",
        "college_type": "Constituent / University College",
        "district": "Hassan",
        "state": "Karnataka",
        "university": "University of Agricultural Sciences, Bangalore (Id: U-0248)"
    },
    {
        "college_name": "Agriculture College, V C Farm, Mandya (Id: C-36459)",
        "college_type": "Constituent / University College",
        "district": "Mandya",
        "state": "Karnataka",
        "university": "University of Agricultural Sciences, Bangalore (Id: U-0248)"
    },
    {
        "college_name": "Sericulture college,Chinthamani (Id: C-36458)",
        "college_type": "Constituent / University College",
        "district": "Chikkaballapura",
        "state": "Karnataka",
        "university": "University of Agricultural Sciences, Bangalore (Id: U-0248)"
    },
    {
        "college_name": "COLLEGE OF AGRICULTURE,BIJAPUR (Id: C-44535)",
        "college_type": "Constituent / University College",
        "district": "Bijapur",
        "state": "Karnataka",
        "university": "University of Agricultural Sciences, Dharwad (Id: U-0246)"
    },
    {
        "college_name": "COLLEGE OF AGRICULTURE, DHARWAD (Id: C-30813)",
        "college_type": "Constituent / University College",
        "district": "Dharwad",
        "state": "Karnataka",
        "university": "University of Agricultural Sciences, Dharwad (Id: U-0246)"
    },
    {
        "college_name": "COLLEGE OF FORESTRY,SIRSI (Id: C-44536)",
        "college_type": "Constituent / University College",
        "district": "Uttara Kannada",
        "state": "Karnataka",
        "university": "University of Agricultural Sciences, Dharwad (Id: U-0246)"
    },
    {
        "college_name": "COLLEGE OF RURAL HOME SCIENCE,DHARWAD (Id: C-44537)",
        "college_type": "Constituent / University College",
        "district": "Dharwad",
        "state": "Karnataka",
        "university": "University of Agricultural Sciences, Dharwad (Id: U-0246)"
    },
    {
        "college_name": "College of Agriculture,Bheemarayangudi (Id: C-35095)",
        "college_type": "Constituent / University College",
        "district": "Raichur",
        "state": "Karnataka",
        "university": "University of Agricultural Sciences, Raichur (Id: U-0247)"
    },
    {
        "college_name": "College of Agriculture, Raichur (Id: C-35094)",
        "college_type": "Constituent / University College",
        "district": "Raichur",
        "state": "Karnataka",
        "university": "University of Agricultural Sciences, Raichur (Id: U-0247)"
    },
    {
        "college_name": "College of Agril. Engineering, Raichur (Id: C-35093)",
        "college_type": "Constituent / University College",
        "district": "Raichur",
        "state": "Karnataka",
        "university": "University of Agricultural Sciences, Raichur (Id: U-0247)"
    },
    {
        "college_name": "Allahabad Degree College (Id: C-36473)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "University of Allahabad, Allahabad (Id: U-0548)"
    },
    {
        "college_name": "Arya Kanya Degree College (Id: C-36468)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "University of Allahabad, Allahabad (Id: U-0548)"
    },
    {
        "college_name": "Chaudhary Mahadeo Prasad Degree College (Id: C-36480)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "University of Allahabad, Allahabad (Id: U-0548)"
    },
    {
        "college_name": "Ewing Christian College(Autonomous College) (Id: C-36470)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "University of Allahabad, Allahabad (Id: U-0548)"
    },
    {
        "college_name": "Govind Ballabh Pant Social Science Institute (Id: C-36471)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "University of Allahabad, Allahabad (Id: U-0548)"
    },
    {
        "college_name": "Hamidia Girls Degree College (Id: C-36467)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "University of Allahabad, Allahabad (Id: U-0548)"
    },
    {
        "college_name": "Iswar Saran Degree College (Id: C-36474)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "University of Allahabad, Allahabad (Id: U-0548)"
    },
    {
        "college_name": "Jagat Taran Girls Degree College (Id: C-36479)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "University of Allahabad, Allahabad (Id: U-0548)"
    },
    {
        "college_name": "K.P.Training College (Id: C-36478)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "University of Allahabad, Allahabad (Id: U-0548)"
    },
    {
        "college_name": "Rajarshi Tandon Girls Degree College (Id: C-36465)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "University of Allahabad, Allahabad (Id: U-0548)"
    },
    {
        "college_name": "Sanwal Dass Sadan Lal Khanna Girls Degree College (Id: C-36475)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "University of Allahabad, Allahabad (Id: U-0548)"
    },
    {
        "college_name": "Shyama Prasad Mukherji Govt. Degree College (Id: C-36466)",
        "college_type": "Constituent / University College",
        "district": "Allahabad",
        "state": "Uttar Pradesh",
        "university": "University of Allahabad, Allahabad (Id: U-0548)"
    },
    {
        "college_name": "College of Horticulture, Arabhavi (Id: C-35748)",
        "college_type": "Constituent / University College",
        "district": "Belgaum",
        "state": "Karnataka",
        "university": "University of Horticultural Sciences, Bagalkot (Id: U-0245)"
    },
    {
        "college_name": "College of Horticulture, Bagalkot (Id: C-35759)",
        "college_type": "Constituent / University College",
        "district": "Bagalkot",
        "state": "Karnataka",
        "university": "University of Horticultural Sciences, Bagalkot (Id: U-0245)"
    },
    {
        "college_name": "College of Horticulture, Bidar (Id: C-35749)",
        "college_type": "Constituent / University College",
        "district": "Bidar",
        "state": "Karnataka",
        "university": "University of Horticultural Sciences, Bagalkot (Id: U-0245)"
    },
    {
        "college_name": "College of Horticulture, Kolar (Id: C-35753)",
        "college_type": "Constituent / University College",
        "district": "Kolar",
        "state": "Karnataka",
        "university": "University of Horticultural Sciences, Bagalkot (Id: U-0245)"
    },
    {
        "college_name": "College of Horticulture, Koppal (Id: C-35757)",
        "college_type": "Constituent / University College",
        "district": "Koppal",
        "state": "Karnataka",
        "university": "University of Horticultural Sciences, Bagalkot (Id: U-0245)"
    },
    {
        "college_name": "College of Horticulture, Mysore (Id: C-35754)",
        "college_type": "Constituent / University College",
        "district": "Mysore",
        "state": "Karnataka",
        "university": "University of Horticultural Sciences, Bagalkot (Id: U-0245)"
    },
    {
        "college_name": "College of Horticulture, Sirsi (Id: C-35752)",
        "college_type": "Constituent / University College",
        "district": "Uttara Kannada",
        "state": "Karnataka",
        "university": "University of Horticultural Sciences, Bagalkot (Id: U-0245)"
    },
    {
        "college_name": "Govt. College of Education, Srinagar (Id: C-21457)",
        "college_type": "Constituent / University College",
        "district": "Srinagar",
        "state": "Jammu and Kashmir",
        "university": "University of Kashmir, Srinagar (Id: U-0196)"
    },
    {
        "college_name": "Govt. Dental College, Srinagar (Id: C-21425)",
        "college_type": "Constituent / University College",
        "district": "Srinagar",
        "state": "Jammu and Kashmir",
        "university": "University of Kashmir, Srinagar (Id: U-0196)"
    },
    {
        "college_name": "Govt. Medical College Srinagar, (Id: C-21456)",
        "college_type": "Constituent / University College",
        "district": "Srinagar",
        "state": "Jammu and Kashmir",
        "university": "University of Kashmir, Srinagar (Id: U-0196)"
    },
    {
        "college_name": "Institute of Music & Fine Arts Jawahar Nagar, Srinagar (Id: C-21458)",
        "college_type": "Constituent / University College",
        "district": "Srinagar",
        "state": "Jammu and Kashmir",
        "university": "University of Kashmir, Srinagar (Id: U-0196)"
    },
    {
        "college_name": "M.E.T,Teachers Training College Sopore, Kashmir (Id: C-21452)",
        "college_type": "Constituent / University College",
        "district": "Baramula",
        "state": "Jammu and Kashmir",
        "university": "University of Kashmir, Srinagar (Id: U-0196)"
    },
    {
        "college_name": "College of Biotechnology (Id: C-16165)",
        "college_type": "Constituent / University College",
        "district": "Mathura",
        "state": "Uttar Pradesh",
        "university": "UP Pandit Deen Dayal Upadhyaya Veterinary University & Gau-Anusandhan Sansthan, Mathura (Id: U-0534)"
    },
    {
        "college_name": "College of Veterinary Sciences & Animal Husbandry (Id: C-16164)",
        "college_type": "Constituent / University College",
        "district": "Mathura",
        "state": "Uttar Pradesh",
        "university": "UP Pandit Deen Dayal Upadhyaya Veterinary University & Gau-Anusandhan Sansthan, Mathura (Id: U-0534)"
    },
    {
        "college_name": "DDCE,Utkal University (Id: C-39712)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Utkal University, Bhubaneswar (Id: U-0366)"
    },
    {
        "college_name": "M.S. Law College (Id: C-39782)",
        "college_type": "Constituent / University College",
        "district": "Cuttack",
        "state": "Odisha",
        "university": "Utkal University, Bhubaneswar (Id: U-0366)"
    },
    {
        "college_name": "University Law College (Id: C-39668)",
        "college_type": "Constituent / University College",
        "district": "Khordha",
        "state": "Odisha",
        "university": "Utkal University, Bhubaneswar (Id: U-0366)"
    },
    {
        "college_name": "College of Forestry & Hill Agriculture (Id: C-16669)",
        "college_type": "Constituent / University College",
        "district": "Tehri Garhwal",
        "state": "Uttrakhand",
        "university": "UTTARAKHAND UNIVERSITY OF HORTICULTURE AND FORESTRY, BHARSAR (Id: U-0654)"
    },
    {
        "college_name": "VCSG College of Horticulture (Id: C-16674)",
        "college_type": "Constituent / University College",
        "district": "Garhwal",
        "state": "Uttrakhand",
        "university": "UTTARAKHAND UNIVERSITY OF HORTICULTURE AND FORESTRY, BHARSAR (Id: U-0654)"
    },
    {
        "college_name": "SEEMANT INSTITUTE OF TECHNOLOGY (Constituent College of Uttarakhand technical University) (Id: C-21319)",
        "college_type": "Constituent / University College",
        "district": "Pithoragarh",
        "state": "Uttrakhand",
        "university": "Uttrakhand Technical University, Dehradun (Id: U-0566)"
    },
    {
        "college_name": "THDC Institute of Hydropower Engineering & Technology (Constituent College of Uttarakhand technical University) (Id: C-21295)",
        "college_type": "Constituent / University College",
        "district": "Tehri Garhwal",
        "state": "Uttrakhand",
        "university": "Uttrakhand Technical University, Dehradun (Id: U-0566)"
    },
    {
        "college_name": "WOMEN INSTITUTE OF TECHNOLOGY (Id: C-47540)",
        "college_type": "Constituent / University College",
        "district": "Dehradun",
        "state": "Uttrakhand",
        "university": "Uttrakhand Technical University, Dehradun (Id: U-0566)"
    },
    {
        "college_name": "A.S. College, Bikramganj (Id: C-27130)",
        "college_type": "Constituent / University College",
        "district": "Rohtas",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "D.K. College, Dumraon (Id: C-27149)",
        "college_type": "Constituent / University College",
        "district": "Buxar",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "Gram Bharti College, Ramgarh (Id: C-27121)",
        "college_type": "Constituent / University College",
        "district": "Kaimur (Bhabua)",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "H.D. Jain College, Ara (Id: C-27145)",
        "college_type": "Constituent / University College",
        "district": "Bhojpur",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "Jagjeevan College, Ara (Id: C-27147)",
        "college_type": "Constituent / University College",
        "district": "Bhojpur",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "J.L.N. College, Dehri-on-sone (Id: C-27146)",
        "college_type": "Constituent / University College",
        "district": "Rohtas",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "Maharaja College, Ara (Id: C-27122)",
        "college_type": "Constituent / University College",
        "district": "Bhojpur",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "Mahila College, Dalmianagar (Id: C-27132)",
        "college_type": "Constituent / University College",
        "district": "Rohtas",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "M.M. Mahila College, Ara (Id: C-27139)",
        "college_type": "Constituent / University College",
        "district": "Bhojpur",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "M.V. College, Buxar (Id: C-27158)",
        "college_type": "Constituent / University College",
        "district": "Buxar",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "Rohtas Mahila College, Sasaram (Id: C-27164)",
        "college_type": "Constituent / University College",
        "district": "Rohtas",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "S.B. College, Ara (Id: C-27161)",
        "college_type": "Constituent / University College",
        "district": "Bhojpur",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "Shershah College, Sasaram (Id: C-27138)",
        "college_type": "Constituent / University College",
        "district": "Rohtas",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "S.N. College, Shahmal Khairadeo (Id: C-27103)",
        "college_type": "Constituent / University College",
        "district": "Rohtas",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "S.P. Jain College, Sasaram (Id: C-27126)",
        "college_type": "Constituent / University College",
        "district": "Rohtas",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "Sri Shankar College, Sasaram (Id: C-27125)",
        "college_type": "Constituent / University College",
        "district": "Rohtas",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "S.V.P. College, Bhabua (Id: C-27106)",
        "college_type": "Constituent / University College",
        "district": "Kaimur (Bhabua)",
        "state": "Bihar",
        "university": "Veer Kunwar Singh University, Arrah (Id: U-0077)"
    },
    {
        "college_name": "UBDT College of Engineering, Davanagere (Id: C-1366)",
        "college_type": "Constituent / University College",
        "district": "Davanagere",
        "state": "Karnataka",
        "university": "Vesveswaraiah Technological University, Belgaum (Id: U-0249)"
    },
    {
        "college_name": "Vikrama Simhapuri University College (Id: C-24736)",
        "college_type": "Constituent / University College",
        "district": "Sri Potti Sriramulu Nellore",
        "state": "Andhra Pradesh",
        "university": "Vikram Simhapuri University, Nellore (Id: U-0044)"
    },
    {
        "college_name": "Aarupadai Veedu Institute of Technology (Id: C-10224)",
        "college_type": "Constituent / University College",
        "district": "Kancheepuram",
        "state": "Tamil Nadu",
        "university": "VINAYAKA MISSIONs RESEARCH FOUNDATION, SALEM (Id: U-0492)"
    },
    {
        "college_name": "Aarupadai Veedu Medical College and Hospital (Id: C-10217)",
        "college_type": "Constituent / University College",
        "district": "Puducherry",
        "state": "Puducherry",
        "university": "VINAYAKA MISSIONs RESEARCH FOUNDATION, SALEM (Id: U-0492)"
    },
    {
        "college_name": "Vinayaka Mission's Annapoorana College of Nursing (Id: C-10218)",
        "college_type": "Constituent / University College",
        "district": "Salem",
        "state": "Tamil Nadu",
        "university": "VINAYAKA MISSIONs RESEARCH FOUNDATION, SALEM (Id: U-0492)"
    },
    {
        "college_name": "Vinayaka Mission's College of Nursing (Id: C-10226)",
        "college_type": "Constituent / University College",
        "district": "Puducherry",
        "state": "Puducherry",
        "university": "VINAYAKA MISSIONs RESEARCH FOUNDATION, SALEM (Id: U-0492)"
    },
    {
        "college_name": "Vinayaka Mission's College of Nursing (Id: C-10227)",
        "college_type": "Constituent / University College",
        "district": "Karaikal",
        "state": "Puducherry",
        "university": "VINAYAKA MISSIONs RESEARCH FOUNDATION, SALEM (Id: U-0492)"
    },
    {
        "college_name": "Vinayaka Mission's College of Pharmacy (Id: C-10216)",
        "college_type": "Constituent / University College",
        "district": "Salem",
        "state": "Tamil Nadu",
        "university": "VINAYAKA MISSIONs RESEARCH FOUNDATION, SALEM (Id: U-0492)"
    },
    {
        "college_name": "Vinayaka Mission's College of Physiotherapy (Id: C-10220)",
        "college_type": "Constituent / University College",
        "district": "Salem",
        "state": "Tamil Nadu",
        "university": "VINAYAKA MISSIONs RESEARCH FOUNDATION, SALEM (Id: U-0492)"
    },
    {
        "college_name": "Vinayaka Mission's Homeopathic Medical College (Id: C-10225)",
        "college_type": "Constituent / University College",
        "district": "Salem",
        "state": "Tamil Nadu",
        "university": "VINAYAKA MISSIONs RESEARCH FOUNDATION, SALEM (Id: U-0492)"
    },
    {
        "college_name": "Vinayaka Mission's Kirupananda Variyar Arts and Science College (Id: C-10222)",
        "college_type": "Constituent / University College",
        "district": "Salem",
        "state": "Tamil Nadu",
        "university": "VINAYAKA MISSIONs RESEARCH FOUNDATION, SALEM (Id: U-0492)"
    },
    {
        "college_name": "Vinayaka Mission's Kirupananda Variyar Engineering College (Id: C-10214)",
        "college_type": "Constituent / University College",
        "district": "Salem",
        "state": "Tamil Nadu",
        "university": "VINAYAKA MISSIONs RESEARCH FOUNDATION, SALEM (Id: U-0492)"
    },
    {
        "college_name": "Vinayaka Mission's Kirupananda Variyar Medical College and Hospital (Id: C-10219)",
        "college_type": "Constituent / University College",
        "district": "Salem",
        "state": "Tamil Nadu",
        "university": "VINAYAKA MISSIONs RESEARCH FOUNDATION, SALEM (Id: U-0492)"
    },
    {
        "college_name": "Vinayaka Mission's Medical College and Hospital (Id: C-10215)",
        "college_type": "Constituent / University College",
        "district": "Karaikal",
        "state": "Puducherry",
        "university": "VINAYAKA MISSIONs RESEARCH FOUNDATION, SALEM (Id: U-0492)"
    },
    {
        "college_name": "Vinayaka Mission's Sankarachariyar Dental College (Id: C-10221)",
        "college_type": "Constituent / University College",
        "district": "Salem",
        "state": "Tamil Nadu",
        "university": "VINAYAKA MISSIONs RESEARCH FOUNDATION, SALEM (Id: U-0492)"
    },
    {
        "college_name": "VINAYAKA MISSIONS SIKKIM COLLEGE OF ARTS AND SCIENCES (Id: C-47716)",
        "college_type": "Constituent / University College",
        "district": "East District",
        "state": "Sikkim",
        "university": "Vinayaka Missions Sikkim University, Tadong (Id: U-0433)"
    },
    {
        "college_name": "VINAYAKA MISSIONS SIKKIM COLLEGE OF NURSING (Id: C-47717)",
        "college_type": "Constituent / University College",
        "district": "East District",
        "state": "Sikkim",
        "university": "Vinayaka Missions Sikkim University, Tadong (Id: U-0433)"
    },
    {
        "college_name": "VINAYAKA MISSIONS SIKKIM COLLEGE OF PHARMACEUTICAL SCIENCES (Id: C-47718)",
        "college_type": "Constituent / University College",
        "district": "East District",
        "state": "Sikkim",
        "university": "Vinayaka Missions Sikkim University, Tadong (Id: U-0433)"
    },
    {
        "college_name": "ADARSH COLLEGE, RAJDHANWAR, GIRIDIH (Id: C-44452)",
        "college_type": "Constituent / University College",
        "district": "Giridih",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "BALANAND SANSKRIT COLLEGE, DEOGHAR (Id: C-44392)",
        "college_type": "Constituent / University College",
        "district": "Deoghar",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "BOKARO STEEL CITY COLLEGE, BOKARO (Id: C-44380)",
        "college_type": "Constituent / University College",
        "district": "Bokaro",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "B. S. K. COLLEGE, MAITHON, DHANBAD (Id: C-44425)",
        "college_type": "Constituent / University College",
        "district": "Dhanbad",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "CHAS COLLEGE, CHAS, BOKARO (Id: C-44403)",
        "college_type": "Constituent / University College",
        "district": "Bokaro",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "CHATRA COLLEGE, CHATRA (Id: C-44459)",
        "college_type": "Constituent / University College",
        "district": "Chatra",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "GIRIDIH COLLEGE, GIRIDIH (Id: C-44412)",
        "college_type": "Constituent / University College",
        "district": "Giridih",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "GOVT. SANSKRIT COLLEGE, RANCHI (Id: C-44408)",
        "college_type": "Constituent / University College",
        "district": "Ranchi",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "J. J. COLLEGE, JHUMRITELAIYA, KODERMA (Id: C-44402)",
        "college_type": "Constituent / University College",
        "district": "Kodarma",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "J.N.M. SANSKRIT COLLEGE, CHAIBASA (Id: C-44387)",
        "college_type": "Constituent / University College",
        "district": "Pashchimi Singhbhum",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "KATRAS COLLEGE, KATRASGARH, DHANBAD (Id: C-44424)",
        "college_type": "Constituent / University College",
        "district": "Dhanbad",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "K. B. COLLEGE, BERMO, BOKARO (Id: C-44449)",
        "college_type": "Constituent / University College",
        "district": "Bokaro",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "K. B. WOMEN'S COLLEGE, HAZARIBAG (Id: C-44396)",
        "college_type": "Constituent / University College",
        "district": "Hazaribagh",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "MARKHAM COLLEGE OF COMMERCE, HAZARIBAG (Id: C-44414)",
        "college_type": "Constituent / University College",
        "district": "Hazaribagh",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "P. K. ROY MEMORIAL COLLEGE, DHANBAD (Id: C-44376)",
        "college_type": "Constituent / University College",
        "district": "Dhanbad",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "RAMGARH COLLEGE, RAMGARH (Id: C-44415)",
        "college_type": "Constituent / University College",
        "district": "Ramgarh",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "R. K. MAHILA COLLEGE, GIRIDIH (Id: C-44373)",
        "college_type": "Constituent / University College",
        "district": "Giridih",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "R. S. MORE COLLEGE, GOVINDPUR, DHANBAD (Id: C-44386)",
        "college_type": "Constituent / University College",
        "district": "Dhanbad",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "R. S. P. COLLEGE, JHARIYA (Id: C-44401)",
        "college_type": "Constituent / University College",
        "district": "Dhanbad",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "SINDRI COLLEGE, SINDRI, DHANBAD (Id: C-44383)",
        "college_type": "Constituent / University College",
        "district": "Dhanbad",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "S.S.L.N.T MAHILA COLLEGE, DHANBAD (Id: C-44442)",
        "college_type": "Constituent / University College",
        "district": "Dhanbad",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "ST. COLUMBA'S COLLEGE, HAZARIBAG (Id: C-44404)",
        "college_type": "Constituent / University College",
        "district": "Hazaribagh",
        "state": "Jharkhand",
        "university": "Vinoba Bhave University, Hazaribagh (Id: U-0212)"
    },
    {
        "college_name": "Yenepoya Dental College (Id: C-8528)",
        "college_type": "Constituent / University College",
        "district": "Dakshina Kannada",
        "state": "Karnataka",
        "university": "Yenepoya University, Mangalore (Id: U-0250)"
    },
    {
        "college_name": "Yenepoya Medical College (Id: C-8526)",
        "college_type": "Constituent / University College",
        "district": "Dakshina Kannada",
        "state": "Karnataka",
        "university": "Yenepoya University, Mangalore (Id: U-0250)"
    },
    {
        "college_name": "Yenepoya Nursing College (Id: C-8527)",
        "college_type": "Constituent / University College",
        "district": "Dakshina Kannada",
        "state": "Karnataka",
        "university": "Yenepoya University, Mangalore (Id: U-0250)"
    },
    {
        "college_name": "Yenepoya Physiotherapy College (Id: C-8525)",
        "college_type": "Constituent / University College",
        "district": "Dakshina Kannada",
        "state": "Karnataka",
        "university": "Yenepoya University, Mangalore (Id: U-0250)"
    }
]
```

---------------------------------------


##Contributers
* [Minhajshaikh321 ( Lead. Coordinator )](https://github.com/Minhajshaikh321)
* [Juned Chaudhary](https://github.com/jcjunaidchaudhary))



Project Developed at Center of Excellence, SriGuru Institute of Technology

