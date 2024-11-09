def uvicorn_start():
    import uvicorn

    _reload = True
    uvicorn.run(
        'app.main:app',
        host='0.0.0.0',
        port=8000,
        reload=_reload,
    )


if __name__ == '__main__':
    print('server start script')
    uvicorn_start()
