%works like (zodiac(start_month, start_date, end_month))
zodiac(1, 20, 2, 'Aquarius').
zodiac(2, 21, 3, 'Picses').
zodiac(3, 21, 4, 'Aries').
zodiac(4, 21, 5, 'Taurus').
zodiac(5, 21, 6, 'Gemini').
zodiac(6, 21, 7, 'Cancer').
zodiac(7, 23, 8, 'Leo').
zodiac(8, 23, 9, 'Virgo').
zodiac(9, 23, 10, 'Libra').
zodiac(10, 23, 11, 'Scorpio').
zodiac(11, 23, 12, 'Sagittarius').
zodiac(12, 22, 1, 'Carpicorn').

find_zodiac(Date, Month, ZodiacSign) :-
    zodiac(Month, StartDate, EndDate, ZodiacSign),
    (Date >= StartDate; Date =< EndDate).

start :-
    write('Enter the day of the month: '),
    read(Date),
    write('Enter the month of the year: '),
    read(Month),
    (find_zodiac(Date, Month, ZodiacSign) -> 
        write('your zodiac sign is: '), write(ZodiacSign), nl;
        write('Invalid date or month.'), nl).

