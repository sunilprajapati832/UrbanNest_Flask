from app import create_app

# Rename 'app' to 'application'
application = create_app()

if __name__ == "__main__":
    application.run()