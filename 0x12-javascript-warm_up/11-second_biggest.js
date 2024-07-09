#!/usr/bin/node


const FindSecondLargest = (...args) => {
	const integers = args.map(Number).filter(num => Number.isInteger(num));

	if (integers.length === 0 || integers.length === 0)
	{
		console.log(0);
		return;
	}

	const sortedIntegers = integers.sort((a, b) => b - a);

	console.log(sortedIntegers[1]);
};

const args = process.argv.slice(2);
FindSecondLargest(...args);
