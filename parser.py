def run(config: dict):
    # parsing response
    for submission in config['response']:
        if not config['show_unrated'] and 'rating' not in submission['problem']:
            continue
        if 'rating' in submission['problem']:
            if config['min'] and submission['problem']['rating'] < config['min']:
                continue
            if config['max'] and submission['problem']['rating'] > config['max']:
                continue
        contest = submission['problem']['contestId']
        sub_id = submission['id']
        print((submission['id'], submission['verdict'], submission['problem'],
            f"{config['BASE_URL']}/contest/{contest}/submission/{sub_id}"))
