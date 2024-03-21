import click
import json_manager

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', required=True, help='Name of the user')
@click.option('--lastname', required=True, help='Lastname of the user')
@click.pass_context
def new(ctx, name, lastname):
    if not name or not lastname:
        ctx.fail("The name and the lastname are required")
    else:
        data = json_manager.read_json()
        id = len(data) + 1
        user = {'id': id, 'name': name, 'lastname': lastname}
        data.append(user)
        json_manager.write_json(data)
        print(data)

@cli.command()
def users(order_by=None):
    users = json_manager.read_json()
    if order_by:
        users = sorted(users, key=lambda x: x.get(order_by))
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")

@cli.command()
@click.option('--id', required=True, type=int, help='ID of the user to delete')
@click.pass_context
def delete(ctx, id):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == id:
            data.remove(user)
            json_manager.write_json(data)
            print(f"User with ID {id} has been deleted.")
            return
    print(f"User with ID {id} not found.")

@cli.command()
@click.option('--search', required=True, help='Search term (ID or Name)')
@click.pass_context
def search(ctx, search):
    users = json_manager.read_json()
    found = False
    for user in users:
        if str(user['id']) == search or user['name'] == search:
            print(f"{user['id']} - {user['name']} - {user['lastname']}")
            found = True
    if not found:
        print(f"No user found with ID or name: {search}")

if __name__ == '__main__':
    cli()
