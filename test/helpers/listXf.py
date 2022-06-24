listXf = {
    '@@transducer/init': lambda: [],
    '@@transducer/step': lambda acc, x: acc + x,
    '@@transducer/result': lambda x: x
}


listXfPushData = {
    '@@transducer/init': lambda: [],
    '@@transducer/step': lambda acc, x: acc + [x],
    '@@transducer/result': lambda x: x
}
