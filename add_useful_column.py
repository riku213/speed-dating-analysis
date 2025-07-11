def add_useful_columns(df):
    # 年齢差（相手の年齢 - 自分の年齢）のカラムを追加
    df['age_diff'] = df['age_o'] - df['age']
    df[['age_o', 'age', 'age_diff']].head()

    # race, race_o のワンホットエンコーディングカラムを追加
    race_labels = {
        1: 'black',
        2: 'white',
        3: 'latino',
        4: 'asian',
        5: 'native',
        6: 'other'
    }

    for code, label in race_labels.items():
        df[f'race_{label}'] = (df['race'] == code).astype(int)
        df[f'race_{label}_o'] = (df['race_o'] == code).astype(int)

    # 追加したカラムの先頭5行を表示
    df[[f'race_{label}' for label in race_labels.values()] + 
    [f'race_{label}_o' for label in race_labels.values()]].head()

    # field_cd のワンホットエンコーディングカラムを追加
    field_labels = {
        1: 'law',
        2: 'math',
        3: 'social_science',
        4: 'medical_science',
        5: 'engineering',
        6: 'english',
        7: 'history',
        8: 'business',
        9: 'education',
        10: 'science',
        11: 'social_work',
        12: 'undergrad',
        13: 'politics',
        14: 'film',
        15: 'fine_arts',
        16: 'languages',
        17: 'architecture',
        18: 'other'
    }

    for code, label in field_labels.items():
        df[f'field_{label}'] = (df['field_cd'] == code).astype(int)

    # 追加したカラムの先頭5行を表示
    df[[f'field_{label}' for label in field_labels.values()]].head()

    # career_c のワンホットエンコーディングカラムを追加
    career_labels = {
        1: 'lawyer',
        2: 'academic_research',
        3: 'psychologist',
        4: 'doctor_medicine',
        5: 'engineer',
        6: 'creative_arts_entertainment',
        7: 'business_related',
        8: 'real_estate',
        9: 'international_humanitarian',
        10: 'undecided',
        11: 'social_work',
        12: 'speech_pathology',
        13: 'politics',
        14: 'pro_sports_athletics',
        15: 'other',
        16: 'journalism',
        17: 'architecture'
    }

    for code, label in career_labels.items():
        df[f'career_{label}'] = (df['career_c'] == code).astype(int)

    # 追加したカラムの先頭5行を表示
    df[[f'career_{label}' for label in career_labels.values()]].head()
    return df