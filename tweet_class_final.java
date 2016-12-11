//package edu.umkc.lkull.spam_bot;
//package commented for ease of use

import android.util.Log;
import twitter4j.Status;
import twitter4j.Twitter;
import twitter4j.TwitterFactory;
import twitter4j.TwitterException;
import twitter4j.conf.ConfigurationBuilder;
import android.os.AsyncTask;

public class tweet extends AsyncTask<Void, Void, Void> {
    String tweet_text;
    private static final String TAG = "Twitter Bot Tweet Class";
    private static final String ConsumerKey = "ES3ZdaGKDV8KARt9jKOoZT60X";
    private static final String ConsumerSecret = "GtRLJ1Z9vprDl2ewzg04N0HocV5NyHTe0qa6DYXVWZ3alxKluH";
    private static final String AccessToken = "776135201214738432-Gri2R94zYv9RmNtIR7rHUDxCuxOjpaT";
    private static final String AccessTokenSecret = "V3TQ4CkDdKxEzr5yqHYyJfRUfieWZz5WWGBn8RSsf3bOq";


    tweet(String text) { tweet_text = text; }

    protected Void doInBackground(Void...voids)
    {
        try {
            ConfigurationBuilder cb = new ConfigurationBuilder();

            cb.setDebugEnabled(true)
                    .setOAuthConsumerKey(ConsumerKey)
                    .setOAuthConsumerSecret(ConsumerSecret)
                    .setOAuthAccessToken(AccessToken)
                    .setOAuthAccessTokenSecret(AccessTokenSecret);

            TwitterFactory tf = new TwitterFactory(cb.build());
            Twitter twitter = tf.getInstance();

            //Send the tweet and log success or failure
            twitter4j.Status status = twitter.updateStatus(tweet_text);
            String tweet = "Tweeted: " + tweet_text;
            Log.i(TAG, tweet);
        }
        catch (TwitterException e) {
            Log.e(TAG, "Twitter Error");
        }
        catch (Exception e) {
            Log.e(TAG, "General Error: " + e);
        }
    return null;
    }
}
