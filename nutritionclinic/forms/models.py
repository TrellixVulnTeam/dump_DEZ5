from django.db import models

     
class childreg(models.Model):
    date_of_reg = models.CharField(max_length=100,null=True)
    child_id = models.CharField(max_length=100,primary_key=True) 
    child_name = models.CharField(max_length=100,null=True)
    cimage =models.FileField(upload_to='images/', null=True, verbose_name="")
    birth_date = models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=100,null=True)
    age_in_months = models.CharField(max_length=100,null=True)
    age_in_days = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=100,null=True)
    mother_name = models.CharField(max_length=100,null=True)
    mother_s_age = models.CharField(max_length=100,null=True)
    mother_height = models.CharField(max_length=100,null=True) 
    mcontact_no = models.CharField(max_length=100,null=True )
    father_height = models.CharField(max_length=100,null=True) 
    fcontact_no = models.CharField(max_length=100,null=True)
    address_geolocate = models.CharField(max_length=100,null=True)
    no_of_siblings = models.CharField(max_length=100,null=True)
    nmbrbrthrs = models.CharField(max_length=100,null=True)
    nmbrsis = models.CharField(max_length=100,null=True)
    num_deaths_sblngs = models.CharField(max_length=100,null=True)
    cause_deaths_sblngs = models.CharField(max_length=100,null=True)
    dob_last_child = models.CharField(max_length=100,null=True)
    religion = models.CharField(max_length=100,null=True)
    name_of_gynecologist = models.CharField(max_length=100,null=True)
    name_of_pediatrician = models.CharField(max_length=100,null=True)
    institution = models.CharField(max_length=100,null=True)
    specifyothrs = models.CharField(max_length=100,null=True)
    presenceatdelivery = models.CharField(max_length=100,null=True)
    type = models.CharField(max_length=100,null=True)
    gestational = models.CharField(max_length=100,null=True)
    birth_weight = models.CharField(max_length=100,null=True) 
    birth_length_in_cms = models.CharField(max_length=100,null=True) 
    discharge_weight = models.CharField(max_length=100,null=True) 
    conditionatbirth = models.CharField(max_length=100,null=True)
    babytransfertotherhsptl = models.CharField(max_length=100,null=True)
    specifycause = models.CharField(max_length=100,null=True)
    breastcrawlimmediatedone = models.CharField(max_length=100,null=True)
    bfdone = models.CharField(max_length=100,null=True)
    umbilicalcut = models.CharField(max_length=100,null=True)
    vitamink = models.CharField(max_length=100,null=True)
    antenalvisit = models.CharField(max_length=100,null=True)
    breastfeedskill = models.CharField(max_length=100,null=True)
    bywhom = models.CharField(max_length=100,null=True)
    othersspecify = models.CharField(max_length=100,null=True)
    holdduringbreastfeed = models.CharField(max_length=100,null=True)
    onlybrstmilk = models.CharField(max_length=100,null=True)
    besidemilk = models.CharField(max_length=100,null=True)
    whatanythin = models.CharField(max_length=100,null=True)
    anythingspecify = models.CharField(max_length=100,null=True)
    dctrprscribtn = models.CharField(max_length=100,null=True)
    specifyanyone = models.CharField(max_length=100,null=True)
    conditionofmother = models.CharField(max_length=100,null=True)
    kangaroocare = models.CharField(max_length=100,null=True)
    skintouchforhr = models.CharField(max_length=100,null=True)
    specify9_name = models.CharField(max_length=100,null=True)
    babybath = models.CharField(max_length=100,null=True)
    babyvaccine = models.CharField(max_length=100,null=True)
    whichvaccine = models.CharField(max_length=100,null=True)
    breastfeedathome = models.CharField(max_length=100,null=True)
    specifyplace = models.CharField(max_length=100,null=True)
    baseline_weight = models.CharField(max_length=100,null=True)
    weight_percentile = models.CharField(max_length=100,null=True) 
    baseline_height = models.CharField(max_length=100,null=True) 
    length_height_percentile = models.CharField(max_length=100,null=True) 
    head_circumference_cm = models.CharField(max_length=100,null=True) 
    baseline_muac_mm = models.CharField(max_length=100,null=True) 
    baseline_stntd_stats = models.CharField(max_length=100,null=True)
    baseline_uw_status = models.CharField(max_length=100,null=True)
    baseline_wstng_stats = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.child_id;

class immunizatn(models.Model):
    cid = models.ForeignKey(childreg, on_delete=models.CASCADE)
    cname = models.CharField(max_length=100,null=True)
    measles = models.CharField(max_length=100,null=True)
    bcg = models.CharField(max_length=100,null=True)
    hb = models.CharField(max_length=100,null=True)
    opv = models.CharField(max_length=100,null=True)
    opvweeks = models.CharField(max_length=100,null=True)
    msls = models.CharField(max_length=100,null=True)
    opvten = models.CharField(max_length=100,null=True)
    rota = models.CharField(max_length=100,null=True)
    vitmin = models.CharField(max_length=100,null=True)
    rvirs = models.CharField(max_length=100,null=True)
    opvforteen = models.CharField(max_length=100,null=True)
    ipv = models.CharField(max_length=100,null=True)
    mesls = models.CharField(max_length=100,null=True)
    ipvweeks = models.CharField(max_length=100,null=True)
    vitaminfiv = models.CharField(max_length=100,null=True)
    pen = models.CharField(max_length=100,null=True)
    opvboost = models.CharField(max_length=100,null=True)
    thrdose = models.CharField(max_length=100,null=True)
    dpt = models.CharField(max_length=100,null=True)
    vitmina = models.CharField(max_length=100,null=True)
    vitminafr = models.CharField(max_length=100,null=True)
    vitminae8 = models.CharField(max_length=100,null=True)
    pentav = models.CharField(max_length=100,null=True)
    vitamina2 = models.CharField(max_length=100,null=True)
    vitamina6 = models.CharField(max_length=100,null=True)
    pen14 = models.CharField(max_length=100,null=True)
    rota10 = models.CharField(max_length=100,null=True)
    vitamin7 = models.CharField(max_length=100,null=True)

class predlvry(models.Model):
    mother_id = models.CharField(max_length=100,primary_key=True)
    mother_name = models.CharField(max_length=100,null=True)
    mage = models.CharField(max_length=100,null=True)
    mpreprgncywght = models.CharField(max_length=100,null=True)
    mwghtduringprgncy = models.CharField(max_length=100,null=True)
    mheight = models.CharField(max_length=100,null=True)
    moccupation = models.CharField(max_length=100,null=True)
    specifyoccupation = models.CharField(max_length=100,null=True)
    qualify = models.CharField(max_length=100,null=True)
    religion = models.CharField(max_length=100,null=True)
    specifyreligion = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=100,null=True)
    fname = models.CharField(max_length=100,null=True)
    fage = models.CharField(max_length=100,null=True)
    fheight = models.CharField(max_length=100,null=True)
    foccupation = models.CharField(max_length=100,null=True)
    specifyoccuptn = models.CharField(max_length=100,null=True)
    fqualify = models.CharField(max_length=100,null=True)
    number_of_siblings = models.CharField(max_length=100,null=True)
    deathssib = models.CharField(max_length=100,null=True)
    causesib = models.CharField(max_length=100,null=True)
    doblstc = models.CharField(max_length=100,null=True)
    aname = models.CharField(max_length=100,null=True)
    anumber = models.CharField(max_length=100,null=True)
    area = models.CharField(max_length=100,null=True)
    block_name = models.CharField(max_length=100,null=True)
    name_of_phc = models.CharField(max_length=100,null=True)
    subcenter = models.CharField(max_length=100,null=True)
    districthsp =models.CharField(max_length=100,null=True)
    subdistricthsp = models.CharField(max_length=100,null=True)
    Visit_Number = models.CharField(max_length=100,null=True)
    dorvisit = models.CharField(max_length=100,null=True)
    hspreg = models.CharField(max_length=100,null=True)
    hbtstdate = models.CharField(max_length=100,null=True)
    hbvisit = models.CharField(max_length=100,null=True)
    wghtonvisit = models.CharField(max_length=100,null=True)
    ironsyrup = models.CharField(max_length=100,null=True)
    month_iron_started = models.CharField(max_length=100,null=True)
    not_taking_iron_tablet =models.CharField(max_length=100,null=True)
    tabiron = models.CharField(max_length=100,null=True)
    folic = models.CharField(max_length=100,null=True)
    why = models.CharField(max_length=100,null=True)
    needfolicacid = models.CharField(max_length=100,null=True)
    salt = models.CharField(max_length=100,null=True)
    calciumtab = models.CharField(max_length=100,null=True)
    ttdose = models.CharField(max_length=100,null=True)
    secondtt = models.CharField(max_length=100,null=True)
    consumption = models.CharField(max_length=100,null=True)
    workhrs = models.CharField(max_length=100,null=True)
    complications = models.CharField(max_length=100,null=True)
    specify = models.CharField(max_length=100,null=True)
    bfskillanc =models.CharField(max_length=100,null=True)
    nutritionanc = models.CharField(max_length=100,null=True)
    edd = models.CharField(max_length=100,null=True)


class breastfeed(models.Model):
    child_id =models.ForeignKey(childreg, on_delete=models.CASCADE)
    mother_id =models.ForeignKey(predlvry, on_delete=models.CASCADE)
    wash = models.CharField(max_length=100,null=True)
    water = models.CharField(max_length=100,null=True)
    sat = models.CharField(max_length=100,null=True)
    back = models.CharField(max_length=100,null=True)
    shldr = models.CharField(max_length=100,null=True)
    uncvrd = models.CharField(max_length=100,null=True)
    pressure = models.CharField(max_length=100,null=True)
    unwrapped = models.CharField(max_length=100,null=True)
    heldbaby = models.CharField(max_length=100,null=True)
    legstucked = models.CharField(max_length=100,null=True)
    elevatebaby = models.CharField(max_length=100,null=True)
    thumb = models.CharField(max_length=100,null=True)
    wrist = models.CharField(max_length=100,null=True)
    babytummy = models.CharField(max_length=100,null=True)
    head = models.CharField(max_length=100,null=True)
    nose = models.CharField(max_length=100,null=True)
    fullbody = models.CharField(max_length=100,null=True)
    chin = models.CharField(max_length=100,null=True)
    cupped = models.CharField(max_length=100,null=True)
    finger = models.CharField(max_length=100,null=True)
    distance = models.CharField(max_length=100,null=True)
    parallel = models.CharField(max_length=100,null=True)
    compressbaby = models.CharField(max_length=100,null=True)
    equal = models.CharField(max_length=100,null=True)
    avoid = models.CharField(max_length=100,null=True)
    open = models.CharField(max_length=100,null=True)
    mouth = models.CharField(max_length=100,null=True)
    upperlips = models.CharField(max_length=100,null=True)
    lowerlip = models.CharField(max_length=100,null=True)
    latched = models.CharField(max_length=100,null=True)
    chins = models.CharField(max_length=100,null=True)
    lower = models.CharField(max_length=100,null=True)
    fedfrombreast =models.CharField(max_length=100,null=True)
    empty = models.CharField(max_length=100,null=True)
    foremilk = models.CharField(max_length=100,null=True)
    offer = models.CharField(max_length=100,null=True)
    burped = models.CharField(max_length=100,null=True)
    wokeup = models.CharField(max_length=100,null=True)
    used = models.CharField(max_length=100,null=True)
    hunger = models.CharField(max_length=100,null=True)
    nosepressed = models.CharField(max_length=100,null=True)
    latching = models.CharField(max_length=100,null=True)
    brestfeedhrs = models.CharField(max_length=100,null=True)
    bfnyt = models.CharField(max_length=100,null=True)
    growth = models.CharField(max_length=100,null=True)

class zerotosix(models.Model):
    cid =  models.ForeignKey(childreg, on_delete=models.CASCADE)
    cname = models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=100,null=True)
    mother_id = models.ForeignKey(predlvry, on_delete=models.CASCADE)
    mother_name = models.CharField(max_length=100,null=True)
    date_previous_visit = models.CharField(max_length=100,null=True)
    todays_visit_date = models.CharField(max_length=100,null=True)
    cwghtprevisit = models.CharField(max_length=100,null=True)
    chytprevisit = models.CharField(max_length=100,null=True)
    zscoreprevisit = models.CharField(max_length=100,null=True)
    follow_up_date = models.CharField(max_length=100,null=True)
    weight = models.CharField(max_length=100,null=True)
    height = models.CharField(max_length=100,null=True)
    weight_percentile = models.CharField(max_length=100,null=True)
    height_percentile = models.CharField(max_length=100,null=True)
    zscorepercnt = models.CharField(max_length=100,null=True)
    muac_mm = models.CharField(max_length=100,null=True)
    weight_gain_per_day = models.CharField(max_length=100,null=True)
    exclusivebf = models.CharField(max_length=100,null=True)
    no_of_breastfeeding_in_a_day = models.CharField(max_length=100,null=True)
    no_of_breast_feeding_at_night = models.CharField(max_length=100,null=True)
    holdduringbreastfeed = models.CharField(max_length=100,null=True)
    waterneed = models.CharField(max_length=100,null=True)
    honey = models.CharField(max_length=100,null=True)
    besidebm = models.CharField(max_length=100,null=True)
    specify = models.CharField(max_length=100,null=True)
    prepformula = models.CharField(max_length=100,null=True)
    boilwater = models.CharField(max_length=100,null=True)
    catwater = models.CharField(max_length=100,null=True)
    mixing = models.CharField(max_length=100,null=True)
    formula = models.CharField(max_length=100,null=True)
    method = models.CharField(max_length=100,null=True)
    disese =models.CharField(max_length=100,null=True)
    specify33 = models.CharField(max_length=100,null=True)
    incbfmilk = models.CharField(max_length=100,null=True)
    specify11 = models.CharField(max_length=100,null=True)
    incbmsuply = models.CharField(max_length=100,null=True)
    specify22 = models.CharField(max_length=100,null=True)
    anydifficulty = models.CharField(max_length=100,null=True)

class sixtotwothreeyr(models.Model):
    cid =  models.ForeignKey(childreg, on_delete=models.CASCADE)
    cname = models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=100,null=True)
    mother_id = models.ForeignKey(predlvry, on_delete=models.CASCADE)
    mother_name = models.CharField(max_length=100,null=True)
    date_previous_visit = models.CharField(max_length=100,null=True)
    todays_visit_date = models.CharField(max_length=100,null=True)
    Child_s_weight_during_previous_visit = models.CharField(max_length=100,null=True)
    height_of_child_during_previous_visit = models.CharField(max_length=100,null=True)
    heightlenght_of_child_z_scoreduring_previous_visit = models.CharField(max_length=100,null=True)
    follow_up_date = models.CharField(max_length=100,null=True)
    weight = models.CharField(max_length=100,null=True)
    height = models.CharField(max_length=100,null=True)
    weight_percentile = models.CharField(max_length=100,null=True)
    height_percentile = models.CharField(max_length=100,null=True)
    leghth_z_score_percentile = models.CharField(max_length=100,null=True)
    muac_mm = models.CharField(max_length=100,null=True)
    weight_gain_per_day = models.CharField(max_length=100,null=True)
    mbfbaby = models.CharField(max_length=100,null=True)
    no_of_breastfeeding = models.CharField(max_length=100,null=True)
    no_of_breast_feeding_at_night_001 = models.CharField(max_length=100,null=True)
    fud = models.CharField(max_length=100,null=True)
    feedwatr = models.CharField(max_length=100,null=True)
    date_at_complementary_feeding = models.CharField(max_length=100,null=True)
    foodgroups = models.CharField(max_length=100,null=True)
    mlkprdct = models.CharField(max_length=100,null=True)
    specify = models.CharField(max_length=100,null=True)
    grains = models.CharField(max_length=100,null=True)
    specify1 = models.CharField(max_length=100,null=True)
    grainprep = models.CharField(max_length=100,null=True)
    rootstubers = models.CharField(max_length=100,null=True)
    pls = models.CharField(max_length=100,null=True)
    mungdaal =models.CharField(max_length=100,null=True)
    masurdaal =models.CharField(max_length=100,null=True)
    urdaal = models.CharField(max_length=100,null=True)
    chickpedaal = models.CharField(max_length=100,null=True)
    mothdaal = models.CharField(max_length=100,null=True)
    nutseed = models.CharField(max_length=100,null=True)
    specify2 = models.CharField(max_length=100,null=True)
    nutseedpwdr = models.CharField(max_length=100,null=True)
    fleshfud = models.CharField(max_length=100,null=True)
    specify3 = models.CharField(max_length=100,null=True)
    vitaprep = models.CharField(max_length=100,null=True)
    vitaminfruit =models.CharField(max_length=100,null=True)
    othrveg = models.CharField(max_length=100,null=True)
    specify4 = models.CharField(max_length=100,null=True)
    fruitsconsume = models.CharField(max_length=100,null=True)
    specify5 = models.CharField(max_length=100,null=True)
    junkfud = models.CharField(max_length=100,null=True)
    frutprdcts = models.CharField(max_length=100,null=True)
    frutbasedbeverage = models.CharField(max_length=100,null=True)
    smeconfectionary = models.CharField(max_length=100,null=True)
    bakryprdct = models.CharField(max_length=100,null=True)
    hotbeverages = models.CharField(max_length=100,null=True)
    breakfast = models.CharField(max_length=100,null=True)
    otherjunkfud = models.CharField(max_length=100,null=True)
    timesjunkfood =models.CharField(max_length=100,null=True)
    dayjunkfood =models.CharField(max_length=100,null=True)
    consistencyoffud = models.CharField(max_length=100,null=True)
    quantityoffood = models.CharField(max_length=100,null=True)
    sevnmnthfood = models.CharField(max_length=100,null=True)
    atemnthfood = models.CharField(max_length=100,null=True)
    ninmnthfood = models.CharField(max_length=100,null=True)
    tentoelvnmnthfood = models.CharField(max_length=100,null=True)
    twlvtothrtnmnthfood = models.CharField(max_length=100,null=True)

class homevisit(models.Model):
    cid =  models.ForeignKey(childreg, on_delete=models.CASCADE)
    cname = models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=100,null=True)
    mother_name = models.CharField(max_length=100,null=True)
    home_visit_date = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    contact_no = models.CharField(max_length=100,null=True)
    home_visitor_name = models.CharField(max_length=100,null=True)
    typesofam = models.CharField(max_length=100,null=True)
    total_family_member = models.CharField(max_length=100,null=True)
    occupation = models.CharField(max_length=100,null=True)
    famstatus = models.CharField(max_length=100,null=True)
    earningsource = models.CharField(max_length=100,null=True)
    membreducate = models.CharField(max_length=100,null=True)
    homeconstruction = models.CharField(max_length=100,null=True)
    ownvehicle = models.CharField(max_length=100,null=True)
    electronics = models.CharField(max_length=100,null=True)
    homestatus = models.CharField(max_length=100,null=True)
    darinagesys = models.CharField(max_length=100,null=True)
    washroom = models.CharField(max_length=100,null=True)
    neatandclean = models.CharField(max_length=100,null=True)
    behavemthr = models.CharField(max_length=100,null=True)
    holdduringbreastfeed = models.CharField(max_length=100,null=True)
    topfeeding = models.CharField(max_length=100,null=True)
    topfeed = models.CharField(max_length=100,null=True)
    whosugest = models.CharField(max_length=100,null=True)
    drsgst= models.CharField(max_length=100,null=True)
    inlawsgst= models.CharField(max_length=100,null=True)
    mthrsgst= models.CharField(max_length=100,null=True)
    anysgst = models.CharField(max_length=100,null=True)
    handwash = models.CharField(max_length=100,null=True)
    mthrfoloprcs = models.CharField(max_length=100,null=True)
    childhandwash = models.CharField(max_length=100,null=True)
    prsnlhygieneneeds = models.CharField(max_length=100,null=True)
    takescareofchild = models.CharField(max_length=100,null=True)
    anyother1 =models.CharField(max_length=100,null=True)
    fud = models.CharField(max_length=100,null=True)
    mixing = models.CharField(max_length=100,null=True)
    formula = models.CharField(max_length=100,null=True)
    separatefud = models.CharField(max_length=100,null=True)
    powder1 = models.CharField(max_length=100,null=True)
    junkfoodgiven = models.CharField(max_length=100,null=True)
    junkfud = models.CharField(max_length=100,null=True)
    frutprdcts = models.CharField(max_length=100,null=True)
    frutbasedbeverage = models.CharField(max_length=100,null=True)
    smeconfectionary =models.CharField(max_length=100,null=True)
    bakryprdct = models.CharField(max_length=100,null=True)
    hotbeverages = models.CharField(max_length=100,null=True)
    breakfast = models.CharField(max_length=100,null=True)
    otherjunkfud = models.CharField(max_length=100,null=True)
    givesjunkfood = models.CharField(max_length=100,null=True)
    anyother11 = models.CharField(max_length=100,null=True)
    anyaddictionmom = models.CharField(max_length=100,null=True)
    symptoms = models.CharField(max_length=100,null=True)
    symptomschild = models.CharField(max_length=100,null=True)



    
