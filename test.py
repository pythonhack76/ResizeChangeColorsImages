import argparse



if __name__ == '__main__':
    parse = argparse.ArgumentParser(
        description="my project"
    ) 

    parser.add_argument('--num1', help="Number 1", type=float)
    

    #parsa argomnento
    args = parser.parse_args() 