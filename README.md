

## Deployment

This application is set up to be deployed on Google Cloud App Engine. To deploy:

1. Make sure you have the Google Cloud SDK installed and configured.
2. Run:
   ```
   gcloud functions deploy munkchat --runtime python39 --trigger-http --allow-unauthenticated --source ./src
   ```

## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.