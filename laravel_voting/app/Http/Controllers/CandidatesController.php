<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;

class CandidatesController extends Controller
{
    public function createCandidate(Request $request){
        $candidateName= $request->input('candidateName');
        $candidateList= $request->input('candidateList');
        DB::table('candidates')->insert(
            ['name' => $candidateName, 'votes' => 0,'lista'=>$candidateList,'image'=>'default.png']
        );
        return \view('createCandidateForm');
    }

    public function votingPage()
    {
        //check if user has voted or not
        if(!Auth::user()->has_voted){
            
            $candidates = DB::table('candidates')->get();
            return view('voting',['candidates'=>$candidates]);
        }
        else{

            //El usuario ya votó
            //return view('home');
            return \redirect('/')->with('messageProblem','Ya has votado');
        }
       
    }

    public function createCandidateForm()
    {
        return view('createCandidateForm');
    }
    public function castYourVote(Request $request)
    {
        $candidateId = $request->input('candidateId');
        //Guardando votos
        DB::table('candidates')->where('id', $candidateId)
        ->update(['votes' => DB::raw('votes + 1')]);

        DB::table('users')->where('id', Auth::user()->id)
        ->update(['has_voted' => 1]); //1 or 0

        //return but with a message
         return \view('/');
        //return \redirect('/home')->with('message', 'Gracias por votar!');
    }
}
