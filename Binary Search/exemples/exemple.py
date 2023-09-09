tests =[]

# query the number of card using the position or query
test = {
    "input":{
        "card": [20, 100, 32 , 1 , 8,9],
        "query": 8
    },
    "output": 4
}

tests.append(test)


# query occurs in the middle

test ={
    "input":{
        "card": [10, 4, -2,3],
        "query": -2
    }
    ,
    "output": 2
}

# query is the first element
tests.append({
    "input":{
        "card": [10, 4, -2,3],
        "query": 10
    }
    ,
    "output": 0
    }
)

#cards contain just one , element, query
tests.append({
    "input":{
        "card": [10],
        "query": 10
    }
    ,
    "output": 0

})




