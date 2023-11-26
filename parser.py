from bs4 import BeautifulSoup
import re
import csv

def getAdministration(s):
    #Get the administration if exists
    try:
        administration = s[-1]
    except IndexError:
        administration = " "
    return administration

def getNamefromRegExpr(atrr, script_tags):
    #Get the name using Regular Expressions
    pattern = re.compile(r'DataLayerManager\.{}\s*=\s*"([^"]+)"'.format(atrr))
    val = ""
    for script_tag in script_tags:
        script_content = script_tag.get_text()
        match = pattern.search(script_content)
        if match:
            val = match.group(1)
    return val

def getDescription(soup):
    #Get description if exists
    description_section = soup.find('div', class_='course-sections__description')
    if description_section:
        description_title = description_section.find('h2', class_='course-sections__title').text
        description_content = description_section.find('div', class_='course-sections__content').find('div', id='Snippet').text
        return description_content.replace("\n", "")
    else:
        return ""
    
def getFees(soup):
    #Get fees if exists
    fees_section = soup.find('div', class_='course-sections__fees')
    if fees_section:
        fees_title = fees_section.find('h2', class_='course-sections__title').text
        fees_content = fees_section.find('div', class_='course-sections__content').text
        return fees_content.replace("\n", "")
    else:
        return ""
    


def main():
    folder_names = ['page_' + str(i) for i in range(1, 401)]

    master = 0
    masters = []
    for folder in folder_names:
        #Different method to extract the number of page if this has 1, 2 or 3 numbers
        for i in range(15):
            if master < 135:
                num_folder = folder[-1]
            elif master < 1485:
                num_folder = folder[-2] + folder[-1]
            else:
                num_folder = folder[-3] + folder[-2] + folder[-1]
            html_file = "page" + num_folder + "_master" + str(master)
            with open(folder+"/"+html_file + ".html", 'r', encoding='utf-8') as file:
                html_content = file.read()
            
            soup = BeautifulSoup(html_content, 'html.parser')

            #Get all attributes
            script_tags = soup.find_all('script')
            courseName = soup.title.text.strip().split(' at ')[0]
            universityName = getNamefromRegExpr("dynamicInstitutionName", script_tags)
            facultyName = getNamefromRegExpr("dynamicDepartmentName", script_tags)
            isItFullTime = getNamefromRegExpr("dynamicStudyTypes", script_tags).split(",")[0:-1]
            description = getDescription(soup)
            startDate = getNamefromRegExpr("dynamicStudyTerms", script_tags)
            fees = getFees(soup)
            modality = getNamefromRegExpr("dynamicProgrammeTypes", script_tags)
            
            duration_elem = soup.find('span', class_='key-info__duration')
            #Get duration if exists
            if duration_elem:
                duration = duration_elem.text.strip()
            else:
                duration = ""
            
            #Get city if exists
            city_elem = soup.find('a', class_='course-data__city')
            if city_elem:
                city = city_elem.text.strip()
            else:
                city = ""

            country = getNamefromRegExpr("dynamicLocationCountryName", script_tags)
            administration = getAdministration(getNamefromRegExpr("dynamicStudyTypes", script_tags).split(","))
            url_e = soup.find('link', rel='canonical')
            
            #Get URL if it is possible
            if url_e:
                url = url_e.get('href', 'URL not available')
            else:
                url = ""
            
            with open("courses_tsv/course_{}.tsv".format(master), 'a', encoding='utf-8-sig') as w:
                writer = csv.writer(w, delimiter = '\t')
                writer.writerow([courseName, universityName, facultyName, isItFullTime, description, startDate, fees, modality, duration, city, country, administration, url])
            master = master + 1
main()