
def gen_search_path(comic_data, exclusion_data = [], rem_hours=24):


    # TODO: Add validation
    if type(rem_hours) != int:
        raise TypeError("remaining hours must be an integer")
    if rem_hours < 0:
        raise Exception("remaining hours must be positive")

    # combine title and issue
    title = comic_data['name'].replace(" ", "+")
    issue = f"%23{comic_data['number']}"

    # Add Keywords to description
    keywords = '+'.join(comic_data['keywords']).replace(" ", "+")

    # Grades
    grades = "%2C".join(map(str, comic_data['grades']))
    grading_co = "%2C".join(map(str, comic_data['grading_co']))

    # search category
    # TODO Refactor to not use hard coded cat number
    category = "259104"

    # add pricing
    low_price = comic_data['minprice']
    high_price = comic_data['maxprice']

    # print era
    #TODO: Incorp era for comics
    #era = '+'.join(comic_data['era'])

    # exclusions
    exc = comic_data['exclusions'] + exclusion_data
    for kw in comic_data['keywords']:
        if kw in exc:
            exc.remove(kw)
    exclusions = f"{'+'.join(exc).strip().replace(' ', '+')}"

    #time : hard coded to 24 hours
    #ftrt - ending within

    #TODO: Issue keeping buy now
    #ftrv - hours remaining  :  #f"&LH_Time=1&_ftrt=901&_ftrv=24"
    time_remaining = ""  #f"&LH_Time=1&_ftrt=901&_ftrv={rem_hours}"

    #  Build Path ******

    path = f"_nkw={title}+{issue}"

    # TODO : Fix hard coded cert company
    if len(grades) > 0:
        keywords += f"%28{grading_co}%29+%28{grades}%29"

    if len(keywords) > 0:
        path += f"+{keywords}"

    path += f"&_sacat={category}&_udlo={low_price}&_udhi={high_price}"

    #TODO: Update to not use hard coded value for seller location
    path += f"&LH_PrefLoc=3"

    if len(exclusions) > 0:
        path += f"&_ex_kw={exclusions}"

    # TODO: Update to not use hard coded
    path += f"&_sop=1"

    path += time_remaining

    return path

"_dcat=259104" \
"&_udlo=100&_fsrp=1" \
"&_from=R40" \
"&Grade=9%252E0%2520Very%2520Fine%252FNear%2520Mint" \
"&_ipg=240" \
"&_nkw=amazing+spider-man+" \
"&_sacat=259104&_udhi=400" \
"&Professional%2520Grader=Certified%2520Guaranty%2520Company%2520%2528CGC%2529" \
"&_sop=1"

if __name__ == "__main__":
    v = {'name': 'amazing spider-man', 'issue': 300, "era": [], 'keywords': [], 'grades': [9.0, 9.2], 'exclusions': ['other'], 'minprice': 150, 'maxprice': 420}
    exc = ['variant', 'foil']
    r = gen_search_path(v, exc)
    print(r)
