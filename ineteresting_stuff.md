# some stuff i lear about the dataset

## nan values

### in columns:

```
answer_id                           0
date_sent                          43
last_page                          18
start_lang                          0
random_value                        0
sat_edu_sucess                     25
faculty                            25
faculty_other                      79
edu_level                          26
edu_level_other                   128
semester_n                         29
uebung_helpful                     38
uebung_required                    36
materials_helpfull                 36
uebung_required_postpone           37
effective_learning                 35
kurzscript_usage                   56
fullscript_usage                   43
notes_usage                        41
videos_lecture_usage               53
uebeung_sols_usage                 41
books_usage                        41
old_exams_usage                    43
videos_online_usage                41
ai_usage                           40
material_understanding             44
materials_orga                     43
materials_complicated              42
materials_ontime                   44
materials_workload                 44
materials_help                     42
materials_safety                   47
materials_motivation               48
materials_independent_learning     47
materials_learning_stress          47
materials_timewaste                49
materials_safety_exam              48
feedback                          107
```

in rows:

```
[35, 34, 3, 2, 5, 2, 3, 3, 3, 1, 5, 35, 4, 2, 35, 34, 3, 35, 3, 30, 4, 1, 35, 2, 6, 33, 25, 2, 30, 2, 4, 29, 29, 3, 2, 2, 1, 2, 4, 6, 29, 35, 4, 3, 2, 10, 3, 35, 2, 35, 26, 35, 1, 8, 35, 2, 7, 3, 3, 4, 3, 3, 2, 35, 1, 24, 3, 30, 28, 3, 3, 1, 2, 3, 18, 4, 5, 7, 2, 2, 3, 4, 24, 9, 29, 35, 9, 24, 7, 3, 10, 3, 2, 6, 35, 3, 2, 1, 8, 2, 1, 4, 3, 3, 35, 35, 30, 35, 2, 1, 2, 3, 1, 5, 4, 3, 2, 16, 35, 6, 35, 1, 32, 34, 34, 34, 2, 29]
>>> 
```

since we have 35 columns and the first 5 are meta valuesit is save to assume that the ones over 30 nan values are useless. so i have deleted them

## desc metriken
```

                                    mean       std  min   25%  50%  75%   max
sat_edu_sucess                  2.867347  1.080643  1.0  2.00  3.0  4.0   5.0
semester_n                      3.684211  2.115109  1.0  3.00  3.0  5.0  12.0
uebung_helpful                  4.077778  0.902279  1.0  4.00  4.0  5.0   5.0
uebung_required                 3.934783  1.097493  1.0  4.00  4.0  5.0   5.0
materials_helpfull              3.554348  0.918242  2.0  3.00  4.0  4.0   5.0
uebung_required_postpone        3.725275  1.193184  1.0  3.00  4.0  5.0   5.0
effective_learning              4.440860  0.772663  1.0  4.00  5.0  5.0   5.0
kurzscript_usage                2.819444  1.259626  1.0  2.00  3.0  4.0   5.0
fullscript_usage                3.247059  1.317518  1.0  2.00  3.0  5.0   5.0
notes_usage                     3.333333  1.403208  1.0  2.00  3.0  5.0   5.0
videos_lecture_usage            2.640000  1.301143  1.0  2.00  2.0  3.5   5.0
uebeung_sols_usage              4.080460  1.173530  1.0  3.00  5.0  5.0   5.0
books_usage                     2.528736  1.310415  1.0  1.00  2.0  4.0   5.0
old_exams_usage                 3.835294  1.242569  1.0  3.00  4.0  5.0   5.0
videos_online_usage             3.126437  1.179324  1.0  2.00  3.0  4.0   5.0
ai_usage                        3.409091  1.443466  1.0  2.00  3.0  5.0   5.0
material_understanding          3.630952  0.888748  1.0  3.00  4.0  4.0   5.0
materials_orga                  3.517647  0.894584  1.0  3.00  4.0  4.0   5.0
materials_complicated           3.209302  1.138795  1.0  2.00  3.0  4.0   5.0
materials_ontime                3.821429  1.007929  1.0  3.00  4.0  5.0   5.0
materials_workload              3.404762  1.007431  1.0  3.00  3.0  4.0   5.0
materials_help                  3.872093  0.930484  1.0  3.25  4.0  4.0   5.0
materials_safety                3.562500  0.869217  1.0  3.00  4.0  4.0   5.0
materials_motivation            2.887500  1.125018  1.0  2.00  3.0  4.0   5.0
materials_independent_learning  3.827160  0.984760  1.0  3.00  4.0  4.0   5.0
materials_learning_stress       2.851852  1.130388  1.0  2.00  3.0  4.0   5.0
materials_timewaste             3.468354  1.072206  1.0  3.00  4.0  4.0   5.0
materials_safety_exam           3.262500  0.990381  1.0  3.00  3.0  4.0   5.0
```


edu_level_other is also completely nan!!!!