import re


def main():
	pattern = re.compile(r'^([\d]{4})\-\d\d\-\d\d,(.+),(.+),(\d+),(\d+),.*$')
	with open('documents/results_football_games.csv', 'r') as f:
		for line in f:
			res = re.match(pattern, line)
			if res:
				total = int(res.group(4)) + int(res.group(5)) 
				if total > 16:
					print(	'goles: {goals}, {year} {local},{visiting} {local_goals}-{visiting_goals}'.format( 
							goals=total,  
							year=res.group(1),
							local=res.group(2),
							visiting=res.group(3), 
							local_goals=res.group(4),
							visiting_goals=res.group(5)
						)	)


if __name__ == '__main__':
	main()