{% extends 'base.html' %}
{% block title %} Home {% endblock %}
{% block home_active %} class="active" {% endblock %}


{% block home_new_feature %}      
<a class="trigger_popup_fricc neonText newFeature">New Feature</a>

<div class="hover_bkgr_fricc ">
    <span class="helper "></span>
    <div>
        <div class="popupCloseButton ">&times;</div>
        <p style=" font-weight: bold;color:  blue;font-size: 25px; "> Sprint 2 <hr style="margin-top: 9px!important;border: 5px solid;border-radius: 5px;"></p>
        <p style="font-weight: bold;font-size: larger;color: black;">User account page<br/>
          Edit profile page <br />
          Almost compelete shopping process
          Add admin page      <br />
          Add new ticket      <br />
          Edit tickets <br /> </p>

        <p style=" font-weight: bold;color:  blue;font-size: 25px; "> Sprint 3 <hr style="margin-top: 9px!important;border: 5px solid;border-radius: 5px;"></p>
        <p style="font-weight: bold;font-size: larger;color: black;">FAQ page<br/>
           Complete shpping proccess<br />
          
              Filter search result <br />
              Add sold ticket to user history  <br />
           <br /> </p>
    </div>
</div>
{% endblock %}

{% block content %}
        <div class="row row-fix justify-content-sm-center justify-content-lg-end">
          <div class="col-lg-6 col-xxl-5">
            <div class="form-request form-request-modern bg-gray-lighter novi-background">
              <h4>Find your Flight</h4>
              <!-- RD Mailform-->
              <form class="rd-mailform form-fix">
                <div class="row row-20 row-fix">
            
                  <div class="col-sm-12 col-lg-6">
                      <div class="form-wrap form-wrap-validation">
                        <label class="form-label-outside">From</label>
                        <div class="form-wrap form-wrap-inline">
                         
                          <select name="source_name" id="source_name" class="form-input select-filter"  data-minimum-results-for-search="Infinity" name="city">
                            <option value="{{source[0]}}" selected>{{source[0]}}</option>
                            {% for source in source[1:] %}
                            <option id="sourceid" value="{{source}}">{{source}}</option>
                            {% endfor %}
                         </select>


                        </div>
                      </div>
                  </div>

                  <div class="col-sm-12 col-lg-6">
                    <div class="form-wrap form-wrap-validation">
                      <label class="form-label-outside">To</label>
                      <div class="form-wrap form-wrap-inline">
                        <select name="destination_name" id="destination_name" class="form-input select-filter"  data-minimum-results-for-search="Infinity" name="city">
                          <option value="{{destination[0]}}" selected>{{destination[0]}}</option>
                          {% for destination in destination[1:] %}
                          <option id="destinationid" value="{{destination}}">{{destination}}</option>
                          {% endfor %}
                       </select>
                      </div>
                    </div>
                  </div>

                  <div class="col-sm-12">
                    <label class="form-label-outside">Seat_type</label>
                    <div class="form-wrap form-wrap-inline">
                      <select class="form-input select-filter" data-placeholder="All" data-minimum-results-for-search="Infinity" name="city">
                        <option value="{{seat_type[0]}}" selected>{{seat_type[0]}}</option>
                        {% for seat_type in seat_type[1:] %}
                        <option value="{{seat_type}}">{{seat_type}}</option>
                        {% endfor %}
                      </select>
                    </div>
                  </div>

                  
                  <div class="col-sm-12 col-lg-6">
                    <label class="form-label-outside">Depart Date</label>
                    <div class="form-wrap form-wrap-validation">
                      <!-- Select -->
                      <input class="form-input" id="dateForm" name="date" type="text" data-time-picker="date">
                      <label class="form-label" for="dateForm">Choose the date</label>
                      <!--select.form-input.select-filter(data-placeholder="All", data-minimum-results-for-search="Infinity",  name='city')-->
                      <!--  option(value="1") Choose the date-->
                      <!--  option(value="2") Primary-->
                      <!--  option(value="3") Middle-->
                    </div>
                  </div>
                  <div class="col-sm-12 col-lg-6">
                    <label class="form-label-outside">Duration</label>
                    <div class="form-wrap form-wrap-validation">
                      <!-- Select 2-->
                      <select class="form-input select-filter" data-placeholder="All" data-minimum-results-for-search="Infinity" name="duration">
                        <option value="1">Any length</option>
                        <option value="2">2 days</option>
                        <option value="3">3 days</option>
                        <option value="4">4 days</option>
                      </select>
                    </div>
                  </div>

                  
                  <div class="col-lg-6">
                    <label class="form-label-outside">Adults</label>
                    <div class="form-wrap form-wrap-modern">
                      <input class="form-input input-append" id="form-element-stepper" type="number" min="0" max="300" value="2">
                    </div>
                  </div>
                  <div class="col-lg-6">
                    <label class="form-label-outside">Children</label>
                    <div class="form-wrap form-wrap-modern">
                      <input class="form-input input-append" id="form-element-stepper-1" type="number" min="0" max="300" value="0">
                    </div>
                  </div>
                </div>

                <form action="/search_post">

                  <select name="source_name" id="source_name">
                    {% for source in source %}
                    <option id="sourceid" value="{{source}}">{{source}}</option>
                    {% endfor %}
                 </select>

                 
                <div class="form-wrap form-button "><a class="button button-block button-secondary" id="search"
                  
                  href = {{ url_for('auth.search_post', source = source[0] ) }}
                 
                  >Search Flights</a></div>
                </form>
          
              </form>
            </div>
          </div>
        </div>
     
{% endblock %}