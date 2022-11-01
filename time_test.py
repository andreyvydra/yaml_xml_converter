import time
import main
import main_regex
import main_libraries
from settings import INPUT_FILENAME, TEST_OUTPUT_FILENAME

if __name__ == '__main__':
    print("_________TEST 1_________")
    start = time.time()
    converter = main.Converter(INPUT_FILENAME, TEST_OUTPUT_FILENAME)
    converter.convert()
    print(f"Main converter - {(time.time() * 100 - start * 100)}")

    start = time.time()
    converter = main_regex.Converter(INPUT_FILENAME, TEST_OUTPUT_FILENAME)
    converter.convert()
    print(f"Regex converter - {(time.time() * 100 - start * 100)}")

    start = time.time()
    main_libraries.main(INPUT_FILENAME, TEST_OUTPUT_FILENAME)
    print(f"Libraries converter - {(time.time() * 100 - start * 100)}")

    print("_________TEST 2_________")
    start = time.time()
    for _ in range(50):
        converter = main.Converter(INPUT_FILENAME, TEST_OUTPUT_FILENAME)
        converter.convert()
    print(f"Main converter - {(time.time() - start)}")

    start = time.time()
    for _ in range(50):
        converter = main_regex.Converter(INPUT_FILENAME, TEST_OUTPUT_FILENAME)
        converter.convert()
    print(f"Regex converter - {(time.time() - start)}")

    start = time.time()
    for _ in range(50):
        main_libraries.main(INPUT_FILENAME, TEST_OUTPUT_FILENAME)
    print(f"Library converter - {(time.time() - start)}")
