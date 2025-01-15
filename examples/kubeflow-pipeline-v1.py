from kfp import components
from kfp import dsl


def random_num(low: int, high: int) -> int:
    """Generate a random number between low and high."""
    import random
    return random.randint(low, high)


def flip_coin() -> str:
    """Flip a coin and output heads or tails randomly."""
    import random
    return 'heads' if random.randint(0, 1) == 0 else 'tails'


def print_msg(msg: str):
    """Print a message."""
    print(msg)


# TODO: Create a component from the flip_coin function
flip_coin_op = components.create_component_from_func(
    flip_coin, base_image='registry.access.redhat.com/ubi9/python-39')

# TODO: Create a component from the print_msg function
print_op = components.create_component_from_func(
    print_msg, base_image='registry.access.redhat.com/ubi9/python-39')

# TODO: Create a component from the random_num function
random_num_op = components.create_component_from_func(
    random_num, base_image='registry.access.redhat.com/ubi9/python-39')

# TODO: Decorate function to define a pipeline
@dsl.pipeline(
    name='coin-toss-pipeline',
    description='A simple pipeline'
)
def flipcoin_pipeline():
    flip = flip_coin_op()
    # TODO: Add pipeline logic
    with dsl.Condition(flip.output == 'heads', 'heads-result'):
        print_op('Heads!')
        random_number = random_num_op(0, 9)
        with dsl.Condition(random_number.output > 7):
            print_op('A high value!')
        with dsl.Condition(random_number.output <= 7):
            print_op('A low value!')
    with dsl.Condition(flip.output == 'tails', 'tails-result'):
        print_op('Tails result')

if __name__ == "__main__":
    from kfp_tekton.compiler import TektonCompiler
    compiler = TektonCompiler()
    TektonCompiler().compile(flipcoin_pipeline, "output.yaml")
