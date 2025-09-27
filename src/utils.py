def verificaReviewScore(reviewScore):
    if reviewScore > 2:
        return 'Positiva'
    else:
        return 'Negativa'
    
print(verificaReviewScore(4))