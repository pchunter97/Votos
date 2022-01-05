<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\CandidatesController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/



Route::get('/',[CandidatesController::class,'home'])->name('home');

/*Route::get('/home', function () {
    return view('home');
});*/

// Route::get('/createCandidateForm', function () {
//     return view('createCandidateForm');
// });
Route::get('createCandidateForm',[CandidatesController::class,'createCandidateForm'])->name('createCandidateForm');
Route::post('/createCandidate', [CandidatesController::class, 'createCandidate'])->name('createCandidate');
Route::post('/castYourVote', [CandidatesController::class, 'castYourVote'])->name('castYourVote');

Route::get("/voting",[CandidatesController::class, 'votingPage'])->name('votingPage');



Route::middleware(['auth:sanctum', 'verified'])->get('/dashboard', function () {
    return view('dashboard');
})->name('dashboard');
