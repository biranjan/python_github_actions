import nox

@nox.session
def tests(session):
    session.install('pytest')
    session.install('hypothesis')
    session.run('pytest')

@nox.session
def lint(session):
    session.install('pylint')
    session.run('pylint', 'sort_algo.py')