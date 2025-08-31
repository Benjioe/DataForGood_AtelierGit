import unittest
import sys

def main():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName(sys.argv[1])
    runner = unittest.TextTestRunner()

    result = runner.run(suite)

    if result.errors or result.failures:
        red_color = "\033[91m"
        print(red_color + f"Find error : (error: {result.errors}, failure:{result.failures}")
        return 1  # Test échoué → commit mauvais
    else:
        print(f"Tests are green")
        return 0  # Tous les tests passent → commit bon

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        print(f"Erreur pendant les tests : {e}")
        sys.exit(125)  # Test non concluant