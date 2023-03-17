# WWII Vocab
import time
import os
import subprocess
import sys

questions = ['The defintion of Axis Powers: ',
             'The defintion of Allied Powers: ',
             'The defintion of Facism: ',
             'The defintion of Nazi Party: ',
             'The defintion of Totalitarianism: ',
             'The defintion of Appeasement: ',
             'The defintion of Nationalism: ',
             'The defintion of Communism: ',
             'The defintion of Bolsheviks: ',
             'The defintion of Vladimir Lenin: ',
             'The defintion of Refute: ',
             'The defintion of Opposition: ',
             'The defintion of Socialism: ',
             'The defintion of Vengence: ',
             'The defintion of Adolf Hitler: ',
             'The defintion of Woodrow Wilson: ',
             'The defintion of League of Nations: ',
             'The defintion of Isolationism: ',
             'The defintion of Treaty Of Versailles: ',
             'The defintion of Joseph Stalin: ',
             'The defintion of Winston Churchill: ']
definitions = ['the alliance of Germany, Italy, and Japan in WWII',
               'the alliance formed between Britain, France, and Russia during WWI',
               'a totalitarian system of government that focuses on the good of the state rather than on the good of the indiviual citizens',
               'National Socialist Party; facist political part of Adolf Hitler governed on totalitarian lines and advocating German racial superiority',
               'form of government in which the person or party in charge has absolute control over all aspects of life',
               'giving in to agressive demands in order to avoid war',
               'sense of pride and devotion to one\'s nation',
               'economic and political system in which government owns the means of production and controls economic planning',
               'Marxists whose goal was to seize state power and establish a dictatorship of the proletariat; Soviet Communists',
               'Russian revolutionary and found of Bolshevism; he rose to power in Russia following the Russian Revolution in 1917',
               'to prove wrong by argument or evidence : show to be false or erroneous',
               'an act of setting opposite or over against : the condition of being so set',
               'a political and economic system in which society, usually in the form of the government, owns the means of production',
               'punishment inflicted in retaliation for an injury or offense : Retribution',
               'Totalitarian dictator of Germany; his invasion of European countries led to WWI. He espoused notions of racial superiority and was responsible for the mass murder of millions of Jews and others in the Holocaust',
               'Twenty-eighth president of the United States; he proposed the League of Nations after WWI as a part of his Fourteen Points',
               'an internation body of nations formed after WWI to prevent future wars',
               'staying out of the affairs and wars of other nations; the position intially held by the US at the beginning of WWII',
               'treaty ending WWI; required Germany to pay huge war reparations and establish the League of Nations',
               'Totalitarian dictator of the Soviet Union through WWII and created a powerful Soviet sphere of influence in Eastern Europe after the war',
               'British prime minister; he opposed the polciy of appeasement and led Great Britian through WWII']
points = 0
line = '------'
welcome = 'Welcome! Would you like to continue?'

ans1 = input(str(questions[0]).lstrip('[\'').rstrip('\']')+'\na) '+str(definitions[5]).lstrip('[\'').rstrip('\']')+'\nb) '+str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nc) '+str(definitions[12]).lstrip('[\'').rstrip('\']')+'\nd) '+str(definitions[2]).lstrip('[\'').rstrip('\']'))
if ans1 == 'b':
    points += 1
    print('')
    print('Correct!')
    time.sleep(1)
    print(line)
else:
    print('')
    print('Whoops, got that wrong.')
    time.sleep(1)
    print(line)
ans2 = input(str(questions[1]).lstrip('[\'').rstrip('\']')+'\na) '+str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nb) '+str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nc) '+str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nd) '+str(definitions[0]).lstrip('[\'').rstrip('\']'))
if ans2 == 'b':
    points += 1
    print('')
    print('Correct!')
    time.sleep(1)
    print(line)
else:
    print('')
    print('Whoops, got that wrong.')
    time.sleep(1)
    print(line)
ans2 = input(str(questions[2]).lstrip('[\'').rstrip('\']')+'\na) '+str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nb) '+str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nc) '+str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nd) '+str(definitions[0]).lstrip('[\'').rstrip('\']'))
if ans2 == 'b':
    points += 1
    print('')
    print('Correct!')
    time.sleep(1)
    print(line)
else:
    print('')
    print('Whoops, got that wrong.')
    time.sleep(1)
    print(line)
ans2 = input(str(questions[3]).lstrip('[\'').rstrip('\']')+'\na) '+str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nb) '+str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nc) '+str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nd) '+str(definitions[0]).lstrip('[\'').rstrip('\']'))
if ans2 == 'b':
    points += 1
    print('')
    print('Correct!')
    time.sleep(1)
    print(line)
else:
    print('')
    print('Whoops, got that wrong.')
    time.sleep(1)
    print(line)  
ans2 = input(str(questions[4]).lstrip('[\'').rstrip('\']')+'\na) '+str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nb) '+str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nc) '+str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nd) '+str(definitions[0]).lstrip('[\'').rstrip('\']'))
if ans2 == 'b':
    points += 1
    print('')
    print('Correct!')
    time.sleep(1)
    print(line)
else:
    print('')
    print('Whoops, got that wrong.')
    time.sleep(1)
    print(line)  
    
    