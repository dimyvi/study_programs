text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
for i in text:
    if i not in result:
        result[i] = text.count(i)
