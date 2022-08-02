import logging


log = logging.getLogger('bulk_renamer')
logging.basicConfig(
    level=logging.DEBUG,
    format=(
        '[%(asctime)s] %(levelname)s %(module)s '
        '%(funcName)s:%(lineno)d - %(message)s'
    ),
    filename='bulk_renamer.log'
)


def search_files(pat, target_dir):
    """
    Search files returns a list of files found.

    """
    found = []
    log.info(f'Searching for files in {target_dir}')
    log.debug(f'pat - {pat}')
    log.debug(f'target_dir - {target_dir}')
    log.debug(f'found - {found}')
    log.info(f'Found {len(found)} files!')
    return found


def main(xargs):
    log.info('Start processing...')

    log.debug(f'xargs.new_name - {xargs.new_name}')
    log.debug(f'xargs.filter_pat - {xargs.filter_pat}')
    log.debug(f'xargs.target_dir - {xargs.target_dir}')

    # Search for the files
    found = search_files(xargs.filter_pat, xargs.target_dir)

    # Rename each file found

    # Notify the user


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'new_name',
        help=('The new name of the files. '
              'This will be appended with a number.')
    )
    parser.add_argument(
        'filter_pat',
        help='The name pattern to search.'
    )
    parser.add_argument(
        'target_dir',
        help='The directory to search.'
    )

    xargs = parser.parse_args()
    main(xargs)
