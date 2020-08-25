# hamming-code
Python CLI that can run the hamming-code operations: generate a valid binary sequence and validate a given sequence.

## Usage

  `index.py number {generate,validate}`

 - Number: binary sequence representing the number to be used
 - {generate, validate}: operation mode to be used

## Examples

### Generating

    python3 index.py 0101 generate
    
    Generated sequence: 0100101

### Validating

#### Valid sequence

	python3 index.py 0100101 validate
	
	Correct sequence!
	No error was encountered.

#### Invalid sequence

	python3 index.py 0110101 validate
	
	Corrupted sequence.
	Invalid bit encountered at index 2.
	Right sequence would be 0100101
