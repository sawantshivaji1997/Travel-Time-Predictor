package com.example.sawant.ttp1;

import android.graphics.Color;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

import com.jjoe64.graphview.GraphView;
import com.jjoe64.graphview.series.DataPoint;
import com.jjoe64.graphview.series.LineGraphSeries;

import org.json.JSONException;

/**
 * Created by sawant on 26/10/17.
 */

public class graphplot extends AppCompatActivity {

    private Button back;
    /*
    int x[]={480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960, 990, 1020, 1050, 1080, 1110, 1140, 1170, 1200, 1230};
    int y[]={54, 59, 61, 65, 67, 69, 73, 72, 82, 82, 66, 65, 63, 62, 61, 60, 64, 65, 67, 69, 71, 73, 78, 78, 86, 75};
    int z[]={47, 46, 46, 47, 48, 49, 51, 49, 49, 47, 46, 44, 43, 43, 44, 45, 46, 48, 48, 51, 57, 54, 53, 52, 51, 49};
    int w[]={102, 94, 86, 90, 87, 94, 99, 100, 103, 97, 93, 86, 81, 81, 84, 88, 96, 95, 98, 102, 109, 108, 102, 103, 100, 95};
    int bus[]={62, 62, 61, 60, 64, 63, 63, 62, 59, 60, 62, 62, 61, 63, 66, 68, 62, 63, 65, 63, 61, 61, 59, 62, 64, 61};
    */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.graphplot);
        final GraphView graphView=(GraphView) findViewById(R.id.graph);
        graphView.setTitle("Analysis of the Day");
        graphView.getGridLabelRenderer();


        LineGraphSeries<DataPoint> series = null;
        LineGraphSeries<DataPoint> series2 = null;
        LineGraphSeries<DataPoint> series3=null;
        LineGraphSeries<DataPoint> busseries=null;


        try {
            series = new LineGraphSeries<>(getDataPointbest());
            series2 = new LineGraphSeries<>(getDataPointoptimistic());
            series3 = new LineGraphSeries<>(getDataPointpessimistic());
            busseries = new LineGraphSeries<>(getDataPointBus());
        } catch (JSONException e) {
            e.printStackTrace();
        }



        if(MainActivity.pos2==0) {
            graphView.addSeries(series);
            graphView.addSeries(series2);
            graphView.addSeries(series3);


            series.setColor(Color.BLUE);
            series.setDrawDataPoints(true);
            series.setDataPointsRadius(10);
            series.setThickness(10);
            series.setDrawBackground(true);
            series.setBackgroundColor(Color.argb(50, 0, 0, 255));

            series2.setColor(Color.GREEN);
            series2.setDrawDataPoints(true);
            series2.setDataPointsRadius(10);
            series2.setThickness(10);
            series2.setDrawBackground(true);
            series2.setBackgroundColor(Color.argb(100, 0, 255, 0));

            series3.setColor(Color.RED);
            series3.setDrawDataPoints(true);
            series3.setDataPointsRadius(10);
            series3.setThickness(10);
            series3.setDrawBackground(true);
            series3.setBackgroundColor(Color.argb(10, 255, 0, 0));
        }
        else if(MainActivity.pos2==1){
            graphView.addSeries(busseries);
            busseries.setColor(Color.BLUE);
            busseries.setDrawDataPoints(true);
            busseries.setDataPointsRadius(10);
            busseries.setThickness(10);
            busseries.setDrawBackground(true);
            busseries.setBackgroundColor(Color.argb(50, 0, 0, 255));

        }

        graphView.getViewport().setMinX(450);
        graphView.getViewport().setMaxX(1250);

        graphView.getViewport().setYAxisBoundsManual(true);
        graphView.getViewport().setXAxisBoundsManual(true);

        back = (Button) findViewById(R.id.back);

        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });

    }


    private DataPoint[] getDataPointbest() throws JSONException {
        DataPoint[] dp = new DataPoint[MainActivity.Xaxis.length()];
        for(int i=0;i<MainActivity.Xaxis.length();i++)
        {
            dp[i]=new DataPoint(MainActivity.Xaxis.getInt(i),MainActivity.best_guess_array.getInt(i));
        }
        return (dp);
    }


    private DataPoint[] getDataPointoptimistic() throws JSONException {
        DataPoint[] dp = new DataPoint[MainActivity.Xaxis.length()];
        for(int i=0;i<MainActivity.Xaxis.length();i++)
        {
            dp[i]=new DataPoint(MainActivity.Xaxis.getInt(i),MainActivity.optimistic_array.getInt(i));
        }
        return (dp);
    }

    private DataPoint[] getDataPointpessimistic() throws JSONException {
        DataPoint[] dp = new DataPoint[MainActivity.Xaxis.length()];
        for(int i=0;i<MainActivity.Xaxis.length();i++)
        {
            dp[i]=new DataPoint(MainActivity.Xaxis.getInt(i),MainActivity.pessmistic_array.getInt(i));
        }
        return (dp);
    }


    private DataPoint[] getDataPointBus() throws JSONException{
        DataPoint[] dp = new DataPoint[MainActivity.Xaxis.length()];
        for(int i=0;i<MainActivity.Xaxis.length();i++)
        {
            dp[i]=new DataPoint(MainActivity.Xaxis.getInt(i),MainActivity.bus_array.getInt(i));
        }
        return (dp);

    }
}