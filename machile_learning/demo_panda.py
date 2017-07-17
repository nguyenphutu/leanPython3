import pandas as pd

cities = {"name": ["London", "Berlin", "Madrid", "Rome",
                   "Paris", "Vienna", "Bucharest", "Hamburg",
                   "Budapest", "Warsaw", "Barcelona",
                   "Munich", "Milan"],
          "population": [8615246, 3562166, 3165235, 2874038,
                         2273305, 1805681, 1803425, 1760433,
                         1754000, 1740119, 1602386, 1493900,
                         1350680],
          "population2": [8615246, 3562166, 3165235, 2874038,
                         2273305, 1805681, 1803425, 1760433,
                         1754000, 1740119, 1602386, 1493900,
                         1350680],
          "country": ["England", "Germany", "Spain", "Italy",
                      "France", "Austria", "Romania",
                      "Germany", "Hungary", "Poland", "Spain",
                      "Germany", "Italy"]}

dataframe = {'1': ['Rem dolor vel corporis molestiae officia. Odio quibusdam aut optio ad numquam.', 'Assumenda eos ut quo ea enim quod. Maxime quas voluptates odio quidem doloremque. Omnis provident error asperiores quia aut. Atque placeat est excepturi non modi doloremque.', 'Agree', 'Neither Agree or Disagree', 'Strongly Agree', 'Agree', 'Agree', 'Agree', 'Strongly Agree', 'Strongly Agree', 'Neither Agree or Disagree', 'Disagree', 'Neither Agree or Disagree', 'Disagree', 'Agree', 'Disagree', 'Agree', 'Agree', 'Neither Agree or Disagree', 'Strongly Disagree', 'Strongly Disagree', 'Neither Agree or Disagree', 'Disagree', 'Neither Agree or Disagree', 'Strongly Agree', 'Agree', 'Agree', 'Neither Agree or Disagree', 'Strongly Disagree', 'Neither Agree or Disagree', 'Agree', 'Strongly Disagree', 'Agree', 'Vitae quibusdam tempora quod suscipit. Nemo voluptatem sapiente dolorum pariatur corrupti accusamus. At debitis ut rerum. Eligendi debitis molestiae alias fugit doloremque.', 'Black or African American', 'Over $100,000', '6+', 'Did Not Complete High School', '09615', 'Prefer Not to Answer', '48'], '12': ['Voluptate incidunt excepturi praesentium porro doloribus. Vitae enim nulla explicabo temporibus.\nEst at voluptatem assumenda. Ullam sapiente quos molestiae inventore tempora et dolorum veniam.', 'Ab occaecati laborum officia molestias temporibus dolore officia. Reiciendis sed commodi quisquam. Consectetur dolore incidunt odit ipsum.', 'Disagree', 'Neither Agree or Disagree', 'Strongly Agree', 'Neither Agree or Disagree', 'Disagree', 'Agree', 'Strongly Disagree', 'Strongly Agree', 'Disagree', 'Agree', 'Strongly Agree', 'Neither Agree or Disagree', 'Neither Agree or Disagree', 'Disagree', 'Strongly Agree', 'Neither Agree or Disagree', 'Neither Agree or Disagree', 'Strongly Disagree', 'Strongly Agree', 'Agree', 'Strongly Agree', 'Strongly Agree', 'Agree', 'Disagree', 'Agree', 'Strongly Agree', 'Strongly Agree', 'Strongly Agree', 'Strongly Disagree', 'Neither Agree or Disagree', 'Strongly Agree', 'Molestiae minima consequuntur at saepe eligendi aperiam est illo. Debitis quos fugit repudiandae impedit ipsum modi laudantium fugit. Praesentium inventore praesentium ea autem impedit.', 'Asian', '$75,000 - $99,999', '6+', "Bachelor's Degree", '61895', 'Female', '45']}
index  = ['assist_6', 'assist_5', 'assist_4', 'assist_3', 'assist_2', 'assist_1', 'decide_8', 'decide_7', 'decide_6', 'decide_5', 'decide_3', 'decide_2', 'decide_1', 'decide_4', 'assess_7', 'assess_6', 'assess_5', 'assess_4', 'assess_3', 'assess_2', 'assess_1', 'search_7', 'search_6', 'search_5', 'search_4', 'search_3', 'search_2', 'search_1', 'discover_6', 'discover_5', 'discover_4', 'discover_3', 'discover_2', 'discover_1', 'ethnicity', 'annual_household_income', 'num_children', 'education', 'zipcode', 'gender', 'age']
suvey_rseponse = pd.DataFrame(dataframe, index=index).T



writer = pd.ExcelWriter('output.xlsx')
suvey_rseponse.to_excel(writer,'Sheet1')
writer.save()
print(suvey_rseponse['zipcode'])