import random        #random module
import time          #time module
import sys           #sys module

#country list
Country = [
    'United States',
    'Afghanistan',
    'Albania',
    'Algeria',
    'American Samoa',
    'Andorra',
    'Angola',
    'Anguilla',
    'Antarctica',
    'Antigua And Barbuda',
    'Argentina',
    'Armenia',
    'Aruba',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bermuda',
    'Bhutan',
    'Bolivia',
    'Bosnia And Herzegovina',
    'Botswana',
    'Bouvet Island',
    'Brazil',
    'Brunei Darussalam',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Cayman Islands',
    'Central African Rep',
    'Chad',
    'Chile',
    'China',
    'Christmas Island',
    'Cocos Islands',
    'Colombia',
    'Comoros',
    'Congo',
    'Cook Islands',
    'Costa Rica',
    'Cote D`ivoire',
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Falkland Islands (Malvinas)',
    'Faroe Islands',
    'Fiji',
    'Finland',
    'France',
    'French Guiana',
    'French Polynesia',
    'French S. Territories',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Gibraltar',
    'Greece',
    'Greenland',
    'Grenada'
    'Guadeloupe',
    'Guam',
    'Guatemala',
    'Guinea',
    'Guinea-bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hong Kong',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea (North)',
    'Korea (South)',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macau',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Martinique',
    'Mauritania',
    'Mauritius',
    'Mayotte',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montserrat',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'Netherlands Antilles',
    'New Caledonia',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Niue',
    'Norfolk Island',
    'Northern Mariana Islands',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Pitcairn',
    'Poland',
    'Portugal',
    'Puerto Rico',
    'Qatar',
    'Reunion',
    'Romania',
    'Russian Federation',
    'Rwanda',
    'Saint Kitts And Nevis',
    'Saint Lucia',
    'St Vincent/Grenadines',
    'Samoa',
    'San Marino',
    'Sao Tome',
    'Saudi Arabia',
    'Senegal',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'St. Helena',
    'St.Pierre',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syrian Arab Republic',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tokelau',
    'Tonga',
    'Trinidad And Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City State',
    'Venezuela',
    'Viet Nam',
    'Virgin Islands (British)',
    'Virgin Islands (U.S.)',
    'Western Sahara',
    'Yemen',
    'Yugoslavia',
    'Zaire',
    'Zambia',
    'Zimbabwe']

#time delay
a = 2
b = 0.2
c = 0.08

big_jump = float(f'{random.uniform(7.10, 9.00):.2f}')            #jump with crowd/wind boost
jump_ = float(f'{random.uniform(6.80, 8.50):.2f}')               #jump with no crowd/wind boost
final_bigjump = float(f'{random.uniform(7.00, 9.20):.2f}')       #final jump with crowd
final_basicjump = float(f'{random.uniform(7.20, 8.80):.2f}')    #final jump no crowd

def medal_():
    print('We now head to the award ceremony')
    time.sleep(a)
    user_name = input('What name would you like on your medal')
    time.sleep(a)
    print('Here is the announcer awarding', user_name, 'with their medal')
    time.sleep(a)
    print('As you stand on the podium you shed a tear as your national anthem plays for all to hear')
    time.sleep(a)
    print('What a special moment for you and your country')
    time.sleep(a)
    return ('Well congrats on an incredible day! See you next time')
    return quit()

def no_medal():
    print('Well it was\'nt your day to come away with a medal but that is alright')
    time.sleep(a)
    print('Being top eight in the world will be in the record books forever')
    time.sleep(a)
    return ('I hope you enjoyed your time here and will see you next time')
    return quit()

#intro text
def intro():
    print('Today is the big day!')
    time.sleep(a)
    print('You are competing at the Olympics to attempt to win a gold medal for your country.')
    time.sleep(a)
    return 'In order to advance to the long jump finals you must place in the top 8 competitors after your first three jumps'
    time.sleep(a)

#indoor path
def path_indoor():
    print('You probably made a good choice!')
    time.sleep(a)
    print('Now that you are all set to compete, let\'s begin the competition!')
    time.sleep(a)
    print('The crowd has been electric all day and are ready to see you win')
    time.sleep(a)
    print('You have three attempts to make it to finals')
    time.sleep(a)
    print('Oh no!, it looks like you stepped over the board your first two attempts which is a foul and you get no mark')
    time.sleep(a)
    print('This is it, your last chance to make it to finals and you must finish in the top 8 out of the 16 athletes')
    time.sleep(a)
    jump = input('Do you want to get the crowd involved by clapping as you attempt your last jump? yes/no')
    if jump == 'yes':
        print('Your adrenaline is through the roof, you have a much higher chance of getting a big jump!')
        time.sleep(a)
        print('Here comes your jump')
        time.sleep(a)
        print()
        s = '*******jumping*******'
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print()
        print('Wow what a jump! You jumped', big_jump,'meters')
        time.sleep(a)
        print('Let\'s see if that is enough to make the finals')
        time.sleep(a)
        print(bigjump_topeight())

    elif jump == 'no':
        print('You missed out on some adrenaline for an even bigger jump, but that\'s alright')
        time.sleep(a)
        print('Here comes your jump')
        time.sleep(a)
        s = '*******jumping*******'
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print('Wow what a jump! You jumped', jump_, 'meters')
        time.sleep(a)
        print('Let\'s see if that is enough to make the finals')
        time.sleep(a)
        print(jump_topeight())


#outdoor path
def path_outdoor():
    print('Well it must be a lovely day out.... I hope')
    time.sleep(a)
    print('Now that you are all set to compete, let\'s begin the competition!')
    time.sleep(a)
    print('The crowd has been electric all day and are ready to see you win')
    time.sleep(a)
    print('You are now onto your third and final attempt to make the finals')
    time.sleep(a)
    print('It all comes down to this jump')
    time.sleep(a)
    print('UH OH! A huge gust of wind has came out of nowhere')
    time.sleep(a)
    print('You aren\'t sure which way it is blowing so it could either help or hurt you distance')
    time.sleep(a)
    wait = input('Would you like to wait for the wind to pass before your jump? yes or no ')
    if wait == 'yes':
        print('Well it\'s probably best to play it safe')
        time.sleep(a)
        print('Here comes your jump')
        time.sleep(a)
        s = '*******jumping*******'
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print('Wow what a jump! You jumped', jump_, 'meters')
        time.sleep(a)
        print('Let\'s see if that is enough to make the finals')
        time.sleep(a)
        print(jump_topeight())

    elif wait == 'no':
        print('I like the risk, let\'s hope it works out for you')
        time.sleep(a)
        print('Here comes your jump')
        time.sleep(a)
        s = '*******jumping*******'
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print('Wow what a jump! You jumped', big_jump, 'meters')
        time.sleep(a)
        print('Let\'s see if that is enough to make the finals')
        time.sleep(a)
        print(bigjump_topeight())

#competitors list
Competitors = [('Marco', 7.22), ('John', 7.45), ('Jeremiah', 8.01), ('Christian', 6.55), ('Ricardo', 7.31),
               ('Ben', 6.90), ('Pablo', 7.82), ('Gregory', 7.64), ('Alexis', 8.22), ('Travis', 7.10),
               ('Zachary', 6.73), ('Henry', 8.10), ('Leonardo', 7.73), ('Xavier', 8.33), ('Jackson', 6.89)]

#finals jump
def finals_():
    print('Congrats on making it this far but it is not over yet! Your last jumps don\'t count now')
    time.sleep(a)
    print('Your next two jumps did\'nt quite go your way but that\'s alright')
    time.sleep(a)
    print('You still have one more jump to go')
    time.sleep(a)
    print('This ones for all the marbles')
    time.sleep(a)
    print('The crowd is on their feet as they all get ready to see you final jump')
    time.sleep(a)
    final_jump = input('Would you like to use this to your advantage and get them to clap as you attempt your jump')
    time.sleep(a)
    print('Be careful and don\'t get too excited!')
    if final_jump == 'yes':
        print('Wow! you jumped', final_bigjump, 'meters')
        time.sleep(a)
        print('Let\'s see how you did')
        time.sleep(a)
        s = '*******jumping*******'
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        return big_finaljump()
    elif final_jump == 'no':
        print('Wow! you jumped', final_basicjump, 'meters')
        time.sleep(a)
        print('Let\'s see how you did')
        time.sleep(a)
        s = '*******jumping*******'
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        return basic_finaljump()


#bigfinal jump
def big_finaljump():
    if final_bigjump > 8.33:
        print('Wow can you believe it!! You have won the Olympic Gold!')
        return medal_()
    elif 8.33 > final_bigjump > 8.22:
        print('Wow you were so close! Second place and a silver medal is nothing to be ashamed about')
        return medal_()
    elif 8.22 > final_bigjump > 8.10:
        print('You just barely clinched third place and a Bronze medal! Congratulations')
        return medal_()
    elif 8.10 > final_bigjump > 8.01:
        print("You almost had a bronze medal! You made your country proud with a fourth place finish")
        return no_medal()
    elif 8.01 > final_bigjump > 7.82:
        print('Nice! You finished in fifth place, better luck at the next Olympics')
        return no_medal()
    elif 7.82 > final_bigjump > 7.73:
        print('Oh well, sixth place isn\'t too bad! You can always improve')
        return no_medal()
    elif 7.73 > final_bigjump > 7.64:
        print('Sevent place! Not your worst but also not your best')
        return no_medal()
    elif 7.64 > final_bigjump:
        print('ahh... That was not you best effort but still came away with eighth place')
        return no_medal()

#basic final jump
def basic_finaljump():
    if final_basicjump > 8.33:
        print('Wow can you believe it!! You have won the Olympic Gold!')
        return medal_()
    elif 8.33 > final_basicjump > 8.22:
        print('Wow you were so close! Second place and a silver medal is nothing to be ashamed about')
        return medal_()
    elif 8.22 > final_basicjump > 8.10:
        print('You just barely clinched third place and a Bronze medal! Congratulations')
        return medal_()
    elif 8.10 > final_basicjump> 8.01:
        print("You almost had a bronze medal! You made your country proud with a fourth place finish")
        return no_medal()
    elif 8.01 > final_basicjump > 7.82:
        print('Nice! You finished in fifth place, better luck at the next Olympics')
        return no_medal()
    elif 7.82 > final_basicjump > 7.73:
        print('Oh well, sixth place isn\'t too bad! You can always improve')
        return no_medal()
    elif 7.73 > final_basicjump > 7.64:
        print('Not your worst but also not your best')
        return no_medal()
    elif 7.64 > final_basicjump:
        print('ahh... That was not you best effort but still came away with eighth place')
        return no_medal()


#boosted jump
def bigjump_topeight():
    if big_jump > 7.31:
        print('Congrats! you have made it to finals')
        return finals_()
    elif big_jump < 7.31:
        return 'Sorry, looks like you did\'nt quite make the cut, looks like you will have to wait four more years'
        return quit()
#non boosted jump
def jump_topeight():
    if jump_ > 7.31:
        print('Congrats! you have made it to finals')
        return finals_()
    elif jump_ < 7.31:
        return 'Sorry, looks like you did\'nt quite make the cut, looks like you will have to wait four more years'
        return quit()
#api call
import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"Paris"}

headers = {
	"X-RapidAPI-Key": "603bab52aemsh135091de5b58d3ep110253jsn420bddbeeac2",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
fox = response.json()
today_temp = fox['current']['temp_f']

#welcome message
print("Welcome to the Track and Field long jump simulator!")
time.sleep(a)

start_game = input("Would you like to start the game, yes/no ")
#start game loop
while start_game != 'yes' and start_game != 'no':
    print("Invalid response")
    start_game = input("Would you like to start the game, yes/no ")

if start_game == 'yes':
    print(intro())
    team = input('Which country would you like to represent? ')
    time.sleep(a)
    while team not in Country: #country loop
        print('Try capitalizing the first initial of each word and try again ')
        team = input('Which country would you like to represent ')
    if team in Country:
        print("Awesome! The whole Country is supporting you.")
        time.sleep(a)
        print('The Olympics are taking place in Paris! Let\'s check the weather for today')
        time.sleep(a)
        print('It looks like today\'s temperature is', today_temp,'degrees Fahrenheit' )
        time.sleep(a)
        print('There has been a vote to compete either inside or outside and you have the last vote')
        time.sleep(a)
        location = input('Which will you choose? ')
        time.sleep(a)
        if location.lower() == 'inside':
            print(path_indoor())
        elif location.lower() == 'outside':
            print(path_outdoor())
        else:
            print('Please start over')
            quit()


elif start_game == 'no':
    print('Thanks for stopping by, see you next time!')
    quit()
