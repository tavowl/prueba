
types = {
    'I' : 'SUBJECT',  'You' : 'SUBJECT',  'We' : 'SUBJECT',  'They' : 'SUBJECT', 'He' : 'SUBJECT', 'She' : 'SUBJECT', 'Yo' : 'SUBJECT', 'Tu' : 'SUBJECT', 'Nosotros' : 'SUBJECT','Ellos' : 'SUBJECT','El' : 'SUBJECT', 'Ella' :'SUBJECT',
    'play'   :'VERB_Spresent',   'kill'    :'VERB_Spresent',   'study' : 'VERB_Spresent',   'work' :  'VERB_Spresent',
    'trabajo': 'VERB_Spresent',   'trabajas': 'VERB_Spresent',   'trabajan'  : 'VERB_Spresent',   'trabajamos': 'VERB_Spresent',    'trabaja':  'VERB_Spresent',
    'estudio':'VERB_Spresent',   'estudias':'VERB_Spresent',   'estudiamos':'VERB_Spresent',   'estudian'  :'VERB_Spresent',    'estudia':'VERB_Spresent',
    'juego'  : 'VERB_Spresent',   'juegas'  : 'VERB_Spresent',   'jugamos'   : 'VERB_Spresent',   'juegan'    : 'VERB_Spresent',    'juega'  :  'VERB_Spresent',
    'mato'   : 'VERB_Spresent',   'matas'   : 'VERB_Spresent',   'matamos'   : 'VERB_Spresent',   'matan'     : 'VERB_Spresent',    'mata'   :  'VERB_Spresent',
    'estudiaba':'VERB_Spast',  'estudiaste':'VERB_Spast',   'estudiabamos':'VERB_Spast',   'estudiaron'  :'VERB_Spast',  'estudió':'VERB_Spast', 'jugue' : 'VERB_Spast',
    'soy'    : 'VERB_Spresent'  ,   'eres'    : 'VERB_Spresent' ,   'somos'     : 'VERB_Spresent' ,   'son' :  'VERB_Spresent',    'es'     :  'VERB_Spresent'   ,
    'el' : 'WORD', 'la' : 'WORD', 'los' : 'WORD', 'las' : 'WORD', 'a' : 'WORD',  'a' : 'WORD', 'buenos':'good','malos':'bad',
    'bueno':'WORD',    'buena' : 'WORD', 'malo' : 'WORD',    'mala' : 'WORD','corto' : 'WORD',    'corta' : 'WORD',  'largo' : 'WORD',  
    'larga' : 'WORD',    'alto' : 'WORD',    'alta' : 'WORD',  'bajo' : 'WORD',    'baja' : 'WORD',
    'soccer' : 'WORD',  'people' : 'WORD', 'math' : 'WORD', 'hard' : 'WORD','futbol' : 'WORD', 'personas' : 'WORD', 'matematicas' : 'WORD',
    'duro' : 'WORD', 'con' : 'WORD','carro' : 'WORD','with' : 'WORD', 'cat' : 'WORD',  'gato' : 'WORD', 'mientras' : 'WORD',
    'jugando':'VERB_Contpast',   'tocando':'VERB_Contpast',   'estudiando':'VERB_Contpast',   'matando'  :'VERB_Contpast',    'trabajando':'VERB_Contpast',
    'estaba'   : 'VERB_pastToBe'   ,   'estabas'   :'VERB_pastToBe'   ,   'estabamos'   :   'VERB_pastToBe',   'estaban'     :   'VERB_pastToBe',
    'trabajaba' : 'VERB_Spast', 'trabajaste' : 'VERB_Spast' , 'trabajabamos' : 'VERB_Spast' ,  'trabajaron' : 'VERB_Spast' , 'trabajaba' : 'VERB_Spast',
    'mataba':'VERB_Spast','mataste':'VERB_Spast','matamos':'VERB_Spast','mataron':'VERB_Spast','mataba':'VERB_Spast',
    'rojo' : 'WORD', 'roja' : 'WORD', 'azul' : 'WORD', 'amarillo' : 'WORD', 'amarilla' : 'WORD', 'verde' : 'WORD',
    'marron' : 'WORD', 'morado' : 'WORD', 'morada':'WORD', 'pero' : 'WORD' , ' a menos que' : 'WORD','perro':'WORD','casa':'WORD','helado':'WORD','pajaro':'WORD',
    'beisbol':'WORD','basket':'WORD','programacion':'WORD','ingles':'WORD', 'carne':'WORD', 'mi':'WORD',
    'como'   :  'VERB_Spresent',   'comes'   : 'VERB_Spresent' ,   'comemos'   : 'VERB_Spresent' ,   'comen'     :  'VERB_Spresent',    'come'   :  'VERB_Spresent',
    'comia':'VERB_Spast','comias':'VERB_Spast','comiamos':'VERB_Spast','comieron':'VERB_Spast','comio':'VERB_Spast', 'comiendo':'VERB_Contpast',
    'arroz':'WORD','pan':'WORD','papa':'WORD', 'jugaba'  : 'VERB_Spast',   'jugaste'  : 'VERB_Spast',   'jugabamos'   : 'VERB_Spast',   'jugaban'    : 'VERB_Spast', 
}

subject = {
    'I' : 'yo',    'You' : 'tu',    'We' : 'nosotros',    'They' : 'ellos',    'He' : 'el',    'She' : 'ella',
    'Yo' : 'i',    'Tu' : 'you',    'Nosotros' : 'we',    'Ellos' : 'they',    'El' : 'he',    'Ella' :'she',    
}
verbspr= {
    'play'   :'jugar',   'kill'    :'matar',   'study' : 'estudiar',   'work' :  'trabajar',
    'trabajo': 'work',   'trabajas': 'work',   'trabajan'  : 'work',   'trabajamos': 'work',    'trabaja':  'works',
    'estudio':'study',   'estudias':'study',   'estudiamos':'study',   'estudian'  :'study',    'estudia':'studies',
    'juego'  : 'play',   'juegas'  : 'play',   'jugamos'   : 'play',   'juegan'    : 'play',    'juega'  :  'plays',
    'mato'   : 'kill',   'matas'   : 'kill',   'matamos'   : 'kill',   'matan'     : 'kill',    'mata'   :  'kills',
    'soy'    : 'am'  ,   'eres'    : 'are' ,   'somos'     : 'are' ,   'son'       :  'are',    'es'     :  'is'   ,
    'como'   :  'eat',   'comes'   : 'eat' ,   'comemos'   : 'eat' ,   'comen'     :  'eat',    'come'   :  'eats', 
}
verbspast= {
    'estudiaba':'studied',   'estudiaste':'studied',   'estudiabamos':'studied',   'estudiaron'  :'studied', 
    'trabajaba' : 'worked', 'trabajaste' : 'worked' , 'trabajabamos' : 'worked' ,  'trabajaron' : 'worked' ,
    'jugaba'  : 'played',   'jugaste'  : 'played',   'jugabamos'   : 'played',   'jugaban'    : 'played', 
    'mataba':'killed','mataste':'killed','matamos':'killed','mataron':'killed',
    'comia':'ate','comias':'ate','comiamos':'ate','comieron':'ate','comio':'ate',
}
verbpastToBe = {'estaba'   : 'was'   ,   'estabas'   :'were'   ,   'estabamos'   :   'were',   'estaban'     :   'were'}

verbcontpast = {
    'jugando':'playing',   'tocando':'playing',   'estudiando':'studying',   'matando'  :'killing',    'trabajando':'working','comiendo':'eating',
}
#articulos
article= {
    'el' : 'the',
    'la' : 'the',
    'los' : 'the',
    'las' : 'the',
    'a' : 'un',
    'a' : 'una',
}
#abjetivos
adjetive = {
    'bueno':'good',    'buena' : 'good', 'buenos':'good',
    'malo' : 'bad',    'mala' : 'bad', 'malos':'bad',
    'corto' : 'short',    'corta' : 'short',
    'largo' : 'long',    'larga' : 'long',
    'alto' : 'high',    'alta' : 'high',
    'bajo' : 'low',    'baja' : 'low',
    'rojo' : 'red', 'roja' : 'red', 'azul' : 'blue', 'amarillo' : 'yellow', 'amarilla' : 'yellow', 'verde' : 'green',
    'marron' : 'brown', 'morado' : 'purple', 'morada':'purple', 
}
word = {
    
    'mi':'my','soccer' :  'futbol',  'futbol' : 'soccer','beisbol':'baseball','basket':'basketball',
    'people': 'personas',  'personas' : 'people',
    'math':'matematicas',  'matematicas' : 'math', 'programacion':'programming','ingles':'english',
    'hard' : 'duro',       'duro' : 'hard',
    'con' : 'with',        'with' : 'con',
    'el' : 'the',          'la'   :   'the', 
    'carro' : 'car',       'car' : 'carro',
    'cat' : 'gato',        'gato' : 'cat',
    'mientras' : 'while',   'while' :'mientras',
    'pero' : 'but' , ' a menos que' : 'unless',
    'perro':'dog','casa':'house','helado':'ice cream','pajaro':'bird','arroz':'rice','pan':'bread','papa':'potato','carne':'meat',
}