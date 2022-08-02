import random
from time import sleep


def err_handler():
    """
    try:
        # This is the main code
        name = 'asdf'
        age = name + 3 #! exception happens

    except Exception as err:
        # This block will execute if an error occurs.

        # NOTE: variables declared in the try block will
        # not exist here.
        breakpoint()

    """
    try:
        # This is the main code
        name = 'asdf'
        age = name + 3  #! exception happens
        # age = 3
    except TypeError as ex:
        # handle typerrors
        raise
    except NameError as ex:
        # handle typerrors
        raise
    except (IndexError, ImportError) as ex:
        # Handle multiple errors
        raise
    except Exception as ex:  # Use this exception as a catch all
        # This block will execute if an error occurs.

        # NOTE: variables declared in the try block will
        # not exist here.
        raise ex
    else:
        # This block will execute when no exception occurs
        # Use this block for code or functions that depend on the try block
        # code
        msg = f'Hi {name}, you are {age} yrs old.'
        print(msg)
    finally:
        # This block will execute whether the code fails or not
        # Use this block to do any cleanup when an exception occurs
        print('Done.')


def infinite_loop():
    while True:
        try:
            print('Doing nothing...')
            pause = random.randint(0, 3)
            print(f'pausing for {pause}s...')
            sleep(pause)
        except KeyboardInterrupt:
            break
    print('Done!')


def main(xargs):
    breakpoint()
    if xargs.infinite:
        infinite_loop()
    else:
        err_handler()


if __name__ == '__main__':
    # Code placed here will only run when this module
    # is run from the commandline.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-I', '--infinite-loop',
        help='Call the infinite loop func!',
        action='store_true',
    )

    xargs = parser.parse_args()

    main(xargs)
