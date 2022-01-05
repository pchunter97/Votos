@extends ('layouts.main')

@section('content')

<div class="container">
    <form action="{{route('castYourVote')}}" method='post'>
        {{csrf_field()}}
        <fieldset class="form-group" >
            <div class="row" >
                <div class="col-sm-10" style="margin: 0 auto">
                    <h3>Candidatos</h3>
                    
                    @foreach($candidates as $candidate)
                    <div class="form-check">
                    <input class="form-check-input" type="radio" name="candidateId" id="flexRadioDefault1" value="{{$candidate->id}}">
                    <label class="form-check-label" for="flexRadioDefault1">
                        {{$candidate->name}}
                    </label>
                    </div>
                    @endforeach

                    <div class="form-group row">
                        <div class="col-sm-10" style="margin:0 auto">
                            <button type="submit" class="btn btn-primary">Votar</button>
                        </div>
                    </div>

                </div>
            </div>
        </fieldset>
    </form>
</div>

@endsection