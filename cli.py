import click
import json_manager

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name',required = True, help='name of the user')
@click.option('--lastname',required = True, help='lastname of the user')
@click.pass_context
def new(ctx, name, lastname):
    if not name or not lastname:
        ctx.fail("the name and the lastname are required")
    else:
        data = json_manager.read_json()
        id = len(data) + 1
        user = {
            'id':id,
            'name':name,
            'lastname':lastname
        }
        data.append(user)
        json_manager.write_json(data)
        print(data)
    

@cli.command()
def users():
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")




if __name__ == '__main__':
    cli()
    
