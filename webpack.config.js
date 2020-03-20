require('webpack')
const path = require('path')

module.exports = {
  entry: {
    main: path.resolve(__dirname, 'theme/js/main.js'),
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'dist/js'),
    publicPath: '/js/',
  },
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: [{
          loader: 'babel-loader',
          options: {
            presets: [['env', {
              loose: true,
              targets: {browsers: ['last 2 versions']}
            }]]
          }
        }]
      }
    ]
  }
}
