from time import time


def calculate_time_spent(function):
    """calcule le temps que met une fonction à s'executer."""
    def wrapper(*args, **kwargs):
        """Décore la fonction avec un calcul de temps."""
        
        start = time()
        
        result = function(*args, **kwargs)
        
        end = time()
        time_spent = end - start
        print(f"secondes passées: {time_spent:.2f}")
        
        return result
    
    return wrapper
