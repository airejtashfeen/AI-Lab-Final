% Facts: Diseases and their symptoms
disease(dengue, [headache, muscle_pain, bone_or_joint_pain, nausea, vomiting, pain_behind_eyes, swollen_glands, rash]).
disease(measles, [fever, headache, runny_nose, rash]).
disease(covid19, [cough, shortness_of_breath, difficulty_breathing, sore_throat, congestion, runny_nose, loss_of_taste_or_smell, fatigue, muscle_or_body_aches]).
disease(common_cold, [headache, sneezing, sore_throat, runny_nose, chills]).
disease(flu, [fever, headache, runny_nose, body_ache, conjunctivitis, chills, sore_throat, cough, rash]).
disease(mumps, [fever, sore_throat, swollen_glands]).

% Start
start :-
    write('Welcome to the Diagnosis System!'), nl,
    write('Please enter your name: '), nl,
    read(Name),
    write('Please enter your age: '), nl,
    read(Age),
    write('Please enter your gender (male/female): '), nl,
    read(Gender),
    write('Please list your symptoms as a list (e.g., [fever, headache]): '), nl,
    read(Symptoms),
    diagnose(Name, Age, Gender, Symptoms).

% Diagnosis 
diagnose(Name, Age, Gender, Symptoms) :-
    disease(Disease, DiseaseSymptoms),
    subset(DiseaseSymptoms, Symptoms), % Custom subset predicate
    nl, write('Diagnosis for '), write(Name), write(': '), nl,
    write('Age: '), write(Age), nl,
    write('Gender: '), write(Gender), nl,
    write('You have '), write(Disease), write('.'), nl, !.

% If no disease matches
diagnose(_, _, _, _) :-
    write('No record found for your symptoms.'), nl.

disease_matching(symptoms):-
    ( disease(measles, MeaslesSymptoms), subset(MeaslesSymptoms, Symptoms) -> 
    write('Since you have Measles, you also have Dengue'), nl )