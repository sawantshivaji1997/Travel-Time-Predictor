package com.example.sawant.ttp1;


import android.app.Dialog;
import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.TimePicker;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;


public class MainActivity extends AppCompatActivity {

    boolean holiday,buttonswitch=true,checkflag=false,exceptionflag=false;
    private Spinner spinner1,spinner2;
    private Button button1,button2;
    final Context context = this;
    private EditText editTextAddress;
    Switch switch1;
    public static long pos1,pos2;
    int hh,mm,tim=480;
    int cbg=0,cpg=0,cog=0,bus=0;
    //final String editTextAddress="10.42.0.1";
    final int editTextPort=3345;
    public static JSONObject tosend;
    Dialog dialog1;
    String check;
    public JSONObject jsonObjrec;
    public JSONObject dat;
    public static JSONArray best_guess_array,optimistic_array,pessmistic_array,bus_array,Xaxis;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);






        //Get the widgets reference from XML layout
        final TextView tv = (TextView) findViewById(R.id.tv);
        final TimePicker tp = (TimePicker) findViewById(R.id.tp);

        //Set the TextView text color
        tv.setTextColor(Color.parseColor("#3F51B5"));

        //Set the TimePicker view to 24 hour view
        tp.setIs24HourView(true);

        //Set a TimeChangedListener for TimePicker widget
        tp.setOnTimeChangedListener(new TimePicker.OnTimeChangedListener() {
            @Override
            public void onTimeChanged(TimePicker view, int hourOfDay, int minute) {
                //Display the new time to app interface
                if(hourOfDay<8 || hourOfDay>20){
                    tv.setText("Invalid Time");
                    button1.setEnabled(false);
                    button2.setEnabled(false);

                }
                else
                {
                    hh=12;
                    mm=00;
                    String AMPM = "AM";
                    hh=hourOfDay;
                    mm=minute;
                    tim=(hh*60)+mm;
                    if(hourOfDay>11)
                    {
                        hourOfDay = hourOfDay-12;
                        AMPM = "PM";
                    }
                    tv.setText("" + hourOfDay + ":" + minute + ":" + AMPM);
                    button1.setEnabled(true);
                    button2.setEnabled(true);
                }



            }
        });
        addListenerOnButton();




    }

    public void addListenerOnButton() {

        spinner1 = (Spinner) findViewById(R.id.spinner1);
        spinner2 = (Spinner) findViewById(R.id.spinner2);
        button1 = (Button) findViewById(R.id.button1);
        button2 = (Button) findViewById(R.id.button2);
        switch1 = (Switch) findViewById(R.id.switch1);






        /////////////////////////////predict button
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //custom dialogi
                //final Dialog dialog1 = new Dialog(context);
                buttonswitch=false;
                dialog1 =new Dialog(context);
                dialog1.setContentView(R.layout.dialog);
                dialog1.setTitle("Title...");
                dialog1.create();

                //////////get the route
                pos1=spinner1.getSelectedItemId();
                ///////////get the MOT
                pos2=spinner2.getSelectedItemId();
                ///////////get whether holiday or not
                holiday=switch1.isChecked();

                try {
                   tosend= createobj(tim,(pos1+1),(pos2+1),holiday);
                }catch (JSONException e)
                {
                    e.printStackTrace();
                }
                String tosendstr= tosend.toString();
                editTextAddress = (EditText) findViewById(R.id.address);
                check=editTextAddress.getText().toString();
                if(check.equals("")){
                    checkflag=true;
                    check = null;
                    Toast.makeText(MainActivity.this, "PlEASE ENTER THE IP ADDRESS", Toast.LENGTH_SHORT).show();
                }

                ///////////////////////////Sending the data
                if(!checkflag){

                MyClientTask myClientTask = new MyClientTask(editTextAddress.getText().toString(),
                        editTextPort,tosendstr);
                myClientTask.execute();
                checkflag=false;


                ///////////////////////////////////////////////////////////////
                // set the custom dialog components - text, image and button



                Button dialogButton = (Button) dialog1.findViewById(R.id.dialogButtonOK);
                dialogButton.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        buttonswitch=true;
                        dialog1.dismiss();
                    }
                });

                dialog1.show();
            }
            }
        });
        //////////////////////////////analyze the day button
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                pos1=spinner1.getSelectedItemId();
                ///////////get the MOT
                pos2=spinner2.getSelectedItemId();
                ///////////get whether holiday or not
                holiday=switch1.isChecked();
                editTextAddress = (EditText) findViewById(R.id.address);
                check=editTextAddress.getText().toString();
                if(check.equals("")){
                    checkflag=true;
                    check = null;
                    Toast.makeText(MainActivity.this, "PlEASE ENTER THE IP ADDRESS", Toast.LENGTH_SHORT).show();
                }

                try {
                    tosend= createobj(tim,(pos1+1),(pos2+1),holiday);
                }catch (JSONException e)
                {
                    e.printStackTrace();
                }
                if(!checkflag){
                String tosendstr= tosend.toString();
                MyClientTask myClientTask = new MyClientTask(editTextAddress.getText().toString(),
                        editTextPort,tosendstr);
                myClientTask.execute();
                checkflag=false;
            }}

        });


    }
    /////////////////////////////for launching graphplot activity///////////////////////
    private void launchActivity() {


        //////////get the route


        Intent intent = new Intent(this, graphplot.class);
        startActivity(intent);
    }


    private JSONObject createobj(int tim,long rout,long mot, boolean holi) throws JSONException {
        JSONObject dat=new JSONObject();

        dat.put("Time",tim);
        dat.put("Route",rout);
        dat.put("MOT",mot);
        dat.put("Holiday",holi);
        return dat;
    }


    public class MyClientTask extends AsyncTask<Void, Void, Void> {

        String dstAddress;
        int dstPort;
        String response ="";
        String msgToServer;

        MyClientTask(String addr, int port, String msgTo) {
            dstAddress = addr;
            dstPort = port;
            msgToServer = msgTo;
        }

        @Override
        protected Void doInBackground(Void... arg0) {

            Socket socket = null;
            DataOutputStream dataOutputStream = null;
            DataInputStream dataInputStream = null;

            try {
                socket = new Socket(dstAddress, dstPort);
                dataOutputStream = new DataOutputStream(
                        socket.getOutputStream());
                dataInputStream = new DataInputStream(socket.getInputStream());

                if(msgToServer != null){
                    dataOutputStream.writeUTF(msgToServer);
                }

                response += dataInputStream.readLine();

            } catch (UnknownHostException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
                response += "UnknownHostException: " + e.toString();
                exceptionflag=true;
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
                response += "IOException: " + e.toString();
                exceptionflag=true;
            } finally {
                if(!exceptionflag) {
                    response = response.replace("\\x00", "");
                    try {
                        jsonObjrec = new JSONObject(response);
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                    try {
                        dat = jsonObjrec.getJSONObject("fromserver");
                        cbg = dat.getInt("Car_best_guess");
                        cpg = dat.getInt("Car_pess");
                        cog = dat.getInt("Car_opt");
                        bus = dat.getInt("Bus");
                        best_guess_array = dat.getJSONArray("best_guess");
                        optimistic_array = dat.getJSONArray("optimistic");
                        pessmistic_array = dat.getJSONArray("pessimistic");
                        bus_array = dat.getJSONArray("busg");
                        Xaxis = dat.getJSONArray("X_axis");

                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }


                if (socket != null) {
                    try {
                        socket.close();
                    } catch (IOException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                        exceptionflag=true;
                    }
                }

                if (dataOutputStream != null) {
                    try {
                        dataOutputStream.close();
                    } catch (IOException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                        exceptionflag=true;
                    }
                }

                if (dataInputStream != null) {
                    try {
                        dataInputStream.close();
                    } catch (IOException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                        exceptionflag=true;
                    }
                }
            }
            return null;
        }

        @Override
        protected void onPostExecute(Void result) {
            //textResponse.setText(response);

            if(!exceptionflag) {

                if (!buttonswitch) {
                    TextView head = (TextView) dialog1.findViewById(R.id.head);
                    TextView text_best = (TextView) dialog1.findViewById(R.id.text_best);
                    TextView text_opt = (TextView) dialog1.findViewById(R.id.text_opt);
                    TextView text_pess = (TextView) dialog1.findViewById(R.id.text_pess);

                    TextView best_guess = (TextView) dialog1.findViewById(R.id.best_guess);
                    TextView opt_guess = (TextView) dialog1.findViewById(R.id.opt_guess);
                    TextView pess_guess = (TextView) dialog1.findViewById(R.id.pess_guess);


                    if (pos2 == 0) {

                        head.setText("Predicted Time For Car");
                        best_guess.setText("Average Time Required :");
                        text_best.setText(String.valueOf(cbg / 60) + " Hours " + String.valueOf(cbg % 60) + " minutes");
                        opt_guess.setText("Optimum Time Required :");
                        text_opt.setText(String.valueOf(cog / 60) + " Hours " + String.valueOf(cog % 60) + " minutes");
                        pess_guess.setText("Worst Time Required :");
                        text_pess.setText(String.valueOf(cpg / 60) + " Hours " + String.valueOf(cpg % 60) + " minutes");

                    /*
                    text.setText("Predicted Time For Car \nBest Possible Time Required :\n"+
                    String .valueOf(cbg/60)+" Hours "+String.valueOf(cbg%60)+
                    " minutes \nIdeal Time Required :\n"+
                            String .valueOf(cog/60)+" Hours "+String.valueOf(cog%60)+
                    " minutes \nWorst Possible Time Required :\n"+
                            String .valueOf(cpg/60)+" Hours "+String.valueOf(cpg%60)+" minutes ");
                            */
                    } else if (pos2 == 1) {
                    /*
                    text.setText("Predicted Time For Bus \nBest Possible Time Required :\n"+
                        String .valueOf(bus/60)+" Hours "+String.valueOf(bus%60)+
                        " minutes ");
                        */
                        head.setText("Predicted Time For Bus");
                        opt_guess.setText("Required Time:");
                        text_opt.setText(String.valueOf(bus / 60) + " Hours " + String.valueOf(bus % 60) + " minutes");
                    }
                } else {
                    launchActivity();
                }
                exceptionflag=false;
            }
            else {
                TextView best_guess = (TextView) dialog1.findViewById(R.id.best_guess);
                best_guess.setText(response);
                exceptionflag=false;


            }
            //rec=(TextView) findViewById(R.id.rec);
            //rec.setText(response);
            super.onPostExecute(result);
        }


    }



}
