import actions

def sample_responses(input_text):
    
    user_message = str(input_text).lower()
    
    if user_message in ('hello','q','hi','sup'):
        return 'Hello! You are usi1ng the latest version 2.0 of cool_bot!'
    
    if user_message in ('What is your purpose?','What yoy can do?'):
        return 'I can find everything you need in phone book'
    
    if user_message in ('Import contacts'):
        a = sample_responses
        b = sample_responses
        c = sample_responses
        return actions.importer(a,b,c)
        
    if user_message in ('Export contacts'):
        a = sample_responses
        return(actions.exporter(a))
    
    return 'Pleasy type something i can understand'