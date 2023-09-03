#! /usr/bin/env python3

import argparse
import csv
import re
"""
id	related_id	class	type/scale	name	relevance	text	help	language	validation	mandatory	encrypted	other	default	same_default	same_script	allowed_filetypes	alphasort	answer_width	answer_width_bycolumn	array_filter	array_filter_exclude	array_filter_style	assessment_value	category_separator	choice_input_columns	choice_title	commented_checkbox	commented_checkbox_auto	cssclass	date_format	date_max	date_min	display_columns	display_rows	display_type	dropdown_dates	dropdown_dates_minute_step	dropdown_dates_month_style	dropdown_prefix	dropdown_prepostfix	dropdown_separators	dropdown_size	dualscale_headerA	dualscale_headerB	em_validation_q	em_validation_q_tip	em_validation_sq	em_validation_sq_tip	equals_num_value	equation	exclude_all_others	exclude_all_others_auto	hidden	hide_tip	input_boxes	input_size	label_input_columns	location_city	location_country	location_defaultcoordinates	location_mapheight	location_mapservice	location_mapwidth	location_mapzoom	location_nodefaultfromip	location_postal	location_state	max_answers	max_filesize	max_num_of_files	max_num_value	max_num_value_n	max_subquestions	maximum_chars	min_answers	min_num_of_files	min_num_value	min_num_value_n	multiflexible_checkbox	multiflexible_max	multiflexible_min	multiflexible_step	num_value_int_only	numbers_only	other_comment_mandatory	other_numbers_only	other_replace_text	page_break	parent_order	placeholder	prefix	printable_help	public_statistics	random_group	random_order	rank_title	repeat_headings	reverse	samechoiceheight	samelistheight	scale_export	show_comment	show_grand_total	show_title	show_totals	showpopups	slider_accuracy	slider_custom_handle	slider_default	slider_default_set	slider_handle	slider_layout	slider_max	slider_middlestart	slider_min	slider_orientation	slider_rating	slider_reset	slider_reversed	slider_separator	slider_showminmax	statistics_graphtype	statistics_showgraph	statistics_showmap	suffix	text_input_columns	text_input_width	time_limit	time_limit_action	time_limit_countdown_message	time_limit_disable_next	time_limit_disable_prev	time_limit_message	time_limit_message_delay	time_limit_message_style	time_limit_timer_style	time_limit_warning	time_limit_warning_2	time_limit_warning_2_display_time	time_limit_warning_2_message	time_limit_warning_2_style	time_limit_warning_display_time	time_limit_warning_message	time_limit_warning_style	use_dropdown	value_range_allows_missing
		S		sid		158192																																																																																																																																												
		S		gsid		1																																																																																																																																												
		S		admin		"Helio Loureiro"																																																																																																																																												
		S		adminemail		helio@loureiro.eng.br																																																																																																																																												
		S		anonymized		Y																																																																																																																																												
		S		format		G																																																																																																																																												
		S		savetimings		I																																																																																																																																												
		S		template		bootswatch																																																																																																																																												
		S		language		en																																																																																																																																												
		S		additional_languages																																																																																																																																														
		S		datestamp		I																																																																																																																																												
		S		usecookie		I																																																																																																																																												
		S		allowregister		N																																																																																																																																												
		S		allowsave		I																																																																																																																																												
		S		autonumber_start		0																																																																																																																																												
		S		autoredirect		I																																																																																																																																												
		S		allowprev		I																																																																																																																																												
		S		printanswers		I																																																																																																																																												
		S		ipaddr		I																																																																																																																																												
		S		ipanonymize		I																																																																																																																																												
		S		refurl		I																																																																																																																																												
		S		showsurveypolicynotice		0																																																																																																																																												
		S		publicstatistics		I																																																																																																																																												
		S		publicgraphs		I																																																																																																																																												
		S		listpublic		I																																																																																																																																												
		S		htmlemail		Y																																																																																																																																												
		S		sendconfirmation		Y																																																																																																																																												
		S		tokenanswerspersistence		N																																																																																																																																												
		S		assessments		I																																																																																																																																												
		S		usecaptcha		E																																																																																																																																												
		S		usetokens		N																																																																																																																																												
		S		bounce_email		helio@loureiro.eng.br																																																																																																																																												
		S		emailresponseto		inherit																																																																																																																																												
		S		emailnotificationto		inherit																																																																																																																																												
		S		tokenlength		15																																																																																																																																												
		S		showxquestions		I																																																																																																																																												
		S		showgroupinfo		I																																																																																																																																												
		S		shownoanswer		I																																																																																																																																												
		S		showqnumcode		I																																																																																																																																												
		S		bouncetime		0																																																																																																																																												
		S		bounceprocessing		N																																																																																																																																												
		S		showwelcome		I																																																																																																																																												
		S		showprogress		I																																																																																																																																												
		S		questionindex		-1																																																																																																																																												
		S		navigationdelay		-1																																																																																																																																												
		S		nokeyboard		I																																																																																																																																												
		S		alloweditaftercompletion		N																																																																																																																																												
		S		googleanalyticsstyle		0																																																																																																																																												
		S		tokenencryptionoptions																																																																																																																																														
		SL		surveyls_survey_id		158192		de-informal																																																																																																																																										
		SL		surveyls_language		de-informal		de-informal																																																																																																																																										
		SL		surveyls_title		"Beispielfragebogen für Limesurvey EN/FR/DE"		de-informal																																																																																																																																										
		SL		surveyls_description		"Dieser Beispielfragebogen demonstriert alle in Limesurvey vorhanden Fragetypen sowie zusätzliche Frageoptionen."		de-informal																																																																																																																																										
		SL		surveyls_welcometext		"<p>Dies ist die Willkommensnachricht des Fragebogens. Sie kann unter Fragebogeneinstellungen -> Texte angepasst werden.</p>"		de-informal																																																																																																																																										
		SL		surveyls_endtext				de-informal																																																																																																																																										
		SL		surveyls_url		http://www.limesurvey.org		de-informal																																																																																																																																										
		SL		surveyls_urldescription				de-informal																																																																																																																																										
		SL		surveyls_email_invite_subj		"Einladung zur einer Umfrage"		de-informal																																																																																																																																										
		SL		surveyls_email_invite		"Hallo {FIRSTNAME},Hiermit möchten wir dich zu einer Umfrage einladen.Der Titel der Umfrage ist '{SURVEYNAME}''{SURVEYDESCRIPTION}'Um an dieser Umfrage teilzunehmen, klicke bitte auf den unten stehenden Link.Mit freundlichen Grüßen,{ADMINNAME} ({ADMINEMAIL})----------------------------------------------Klicke hier um die Umfrage zu starten:{SURVEYURL}Wenn Du an dieser Umfrage nicht teilnehmen und keine weiteren Erinnerungen erhalten möchtest, klicke bitte auf den folgenden Link:{OPTOUTURL}"		de-informal																																																																																																																																										
		SL		surveyls_email_remind_subj		"Erinnerung an die Teilnahme an einer Umfrage"		de-informal																																																																																																																																										
		SL		surveyls_email_remind		"Hallo {FIRSTNAME},Vor kurzem haben wir Dich zu einer Umfrage eingeladen.Zu unserem Bedauern haben wir bemerkt, dass Du die Umfrage noch nicht ausgefüllt hast. Wir möchten Dir mitteilen, dass die Umfrage noch aktiv ist und würden uns freuen, wenn Du teilnehmen könntest.Der Titel der Umfrage ist '{SURVEYNAME}''{SURVEYDESCRIPTION}'Um an dieser Umfrage teilzunehmen, klicke bitte auf den unten stehenden Link. Mit freundlichen Grüßen,{ADMINNAME} ({ADMINEMAIL})----------------------------------------------Klicken Du hier um die Umfrage zu starten:{SURVEYURL}Wenn Du an dieser Umfrage nicht teilnehmen und keine weiteren Erinnerungen erhalten möchtest, klicke bitte auf den folgenden Link:{OPTOUTURL}"		de-informal																																																																																																																																										
		SL		surveyls_email_register_subj		"Registrierungsbestätigung für Teilnahmeumfrage"		de-informal																																																																																																																																										
		SL		surveyls_email_register		"Hallo {FIRSTNAME},Du (oder jemand, der Deine E-Mail benutzt hat) hat sich für eine Umfrage mit dem Titel {SURVEYNAME} angemeldet.Um an dieser Umfrage teilzunehmen, klicke bitte auf den folgenden Link.nn{SURVEYURL}Wenn Du irgendwelche Fragen zu dieser Umfrage hast oder wenn Du Dich _nicht_ für diese Umfrage angemeldet hast und Du glaubst, dass Dir diese E-Mail irrtümlicherweise zugeschickt worden ist, kontaktiere bitte {ADMINNAME} unter {ADMINEMAIL}."		de-informal																																																																																																																																										
		SL		surveyls_email_confirm_subj		"Bestätigung für die Teilnahme an unserer Umfrage"		de-informal																																																																																																																																										
		SL		surveyls_email_confirm		"Hallo {FIRSTNAME},Vielen Dank für die Teilnahme an der Umfrage mit dem Titel {SURVEYNAME}. Deine Antworten wurden bei uns gespeichert.Wenn du irgendwelche Fragen zu dieser E-Mail hast, kontaktiere bitte {ADMINNAME} unter {ADMINEMAIL}.Mit freundlichen Grüßen,{ADMINNAME}"		de-informal																																																																																																																																										
		SL		surveyls_dateformat		1		de-informal																																																																																																																																										
		SL		surveyls_alias				de-informal																																																																																																																																										
		SL		email_admin_notification_subj		"Antwortabsendung für Umfrage {SURVEYNAME}"		de-informal																																																																																																																																										
		SL		email_admin_notification		"Hallo,Eine neue Antwort wurde für die Umfrage '{SURVEYNAME}' abgegeben.Klicke auf den folgenden Link um die Umfrage neu zu laden:{RELOADURL}Klicke auf den folgenden Link um den Antwortdatensatz anzusehen:{VIEWRESPONSEURL}Klicke auf den folgenden Link um den Antwortdatensatz zu bearbeiten:{EDITRESPONSEURL}Um die Statistik zu sehen, klicke hier:{STATISTICSURL}"		de-informal																																																																																																																																										
		SL		email_admin_responses_subj		"Antwortabsendung für Umfrage %s"		de-informal																																																																																																																																										
		SL		email_admin_responses		"<style type=""text/css"">                                                .printouttable {                                                  margin:1em auto;                                                }                                                .printouttable th {                                                  text-align: center;                                                }                                                .printouttable td {                                                  border-color: #ddf #ddf #ddf #ddf;                                                  border-style: solid;                                                  border-width: 1px;                                                  padding:0.1em 1em 0.1em 0.5em;                                                }                                                .printouttable td:first-child {                                                  font-weight: 700;                                                  text-align: right;                                                  padding-right: 5px;                                                  padding-left: 5px;                                                }                                                .printouttable .printanswersquestion td{                                                  background-color:#F7F8FF;                                                }                                                .printouttable .printanswersquestionhead td{                                                  text-align: left;                                                  background-color:#ddf;                                                }                                                .printouttable .printanswersgroup td{                                                  text-align: center;                                                          font-weight:bold;                                                  padding-top:1em;                                                }                                                </style>Hallo,Eine neue Antwort wurde für die Umfrage '{SURVEYNAME}' abgegeben.Klicke auf den folgenden Link um die Umfrage neu zu laden:{RELOADURL}Klicke auf den folgenden Link um den Antwortdatensatz anzusehen:{VIEWRESPONSEURL}Klicke auf den folgenden Link um den Antwortdatensatz zu bearbeiten:{EDITRESPONSEURL}Um die Statistik zu sehen, klicke hier:{STATISTICSURL}Die folgenden Antworten wurden vom Teilnehmer gegeben:{ANSWERTABLE}"		de-informal																																																																																																																																										
		SL		surveyls_numberformat		0		de-informal																																																																																																																																										
		SL		surveyls_survey_id		158192		en																																																																																																																																										
		SL		surveyls_language		en		en																																																																																																																																										
		SL		surveyls_title		"Sample LimeSurvey"		en																																																																																																																																										
		SL		surveyls_description		"This survey show all question type of LimeSurvey with some option"		en																																																																																																																																										
		SL		surveyls_welcometext		"<p>This is the welcome text for the survey! You can can edit it in the survey properties.</p>"		en																																																																																																																																										
		SL		surveyls_endtext		"<p>This is the end message for the survey! A good place to thank you to answer to this survey.</p>"		en																																																																																																																																										
		SL		surveyls_url		http://www.limesurvey.org		en																																																																																																																																										
		SL		surveyls_urldescription		"The end URL description of your survey. This URL can be automatically load when survey is completed."		en																																																																																																																																										
		SL		surveyls_email_invite_subj		"Invitation to participate in survey"		en																																																																																																																																										
		SL		surveyls_email_invite		"Dear {FIRSTNAME},<br /><br />You have been invited to participate in a survey.<br /><br />The survey is titled:<br />""{SURVEYNAME}""<br /><br />""{SURVEYDESCRIPTION}""<br /><br />To participate, please click on the link below.<br /><br />Sincerely,<br /><br />{ADMINNAME} ({ADMINEMAIL})<br /><br />----------------------------------------------<br />Click here to do the survey:<br />{SURVEYURL}<br /><br />If you do not want to participate in this survey and don't want to receive any more invitations please click the following link:<br />{OPTOUTURL}"		en																																																																																																																																										
		SL		surveyls_email_remind_subj		"Reminder to participate in survey"		en																																																																																																																																										
		SL		surveyls_email_remind		"Dear {FIRSTNAME},<br /><br />Recently we invited you to participate in a survey.<br /><br />We note that you have not yet completed the survey, and wish to remind you that the survey is still available should you wish to take part.<br /><br />The survey is titled:<br />""{SURVEYNAME}""<br /><br />""{SURVEYDESCRIPTION}""<br /><br />To participate, please click on the link below.<br /><br />Sincerely,<br /><br />{ADMINNAME} ({ADMINEMAIL})<br /><br />----------------------------------------------<br />Click here to do the survey:<br />{SURVEYURL}<br /><br />If you do not want to participate in this survey and don't want to receive any more invitations please click the following link:<br />{OPTOUTURL}"		en																																																																																																																																										
		SL		surveyls_email_register_subj		"Survey registration confirmation"		en																																																																																																																																										
		SL		surveyls_email_register		"Dear {FIRSTNAME},<br /><br />You, or someone using your email address, have registered to participate in an online survey titled {SURVEYNAME}.<br /><br />To complete this survey, click on the following URL:<br /><br />{SURVEYURL}<br /><br />If you have any questions about this survey, or if you did not register to participate and believe this email is in error, please contact {ADMINNAME} at {ADMINEMAIL}."		en																																																																																																																																										
		SL		surveyls_email_confirm_subj		"Confirmation of completed survey"		en																																																																																																																																										
		SL		surveyls_email_confirm		"Dear {FIRSTNAME},<br /><br />This email is to confirm that you have completed the survey titled {SURVEYNAME} and your response has been saved. Thank you for participating.<br /><br />If you have any further questions about this email, please contact {ADMINNAME} at {ADMINEMAIL}.<br /><br />Sincerely,<br /><br />{ADMINNAME}"		en																																																																																																																																										
		SL		surveyls_dateformat		5		en																																																																																																																																										
		SL		surveyls_alias				en																																																																																																																																										
		SL		email_admin_notification_subj		"Response submission for survey {SURVEYNAME}"		en																																																																																																																																										
		SL		email_admin_notification		"Hello,<br /><br />A new response was submitted for your survey '{SURVEYNAME}'.<br /><br />Click the following link to reload the survey:<br />{RELOADURL}<br /><br />Click the following link to see the individual response:<br />{VIEWRESPONSEURL}<br /><br />Click the following link to edit the individual response:<br />{EDITRESPONSEURL}<br /><br />View statistics by clicking here:<br />{STATISTICSURL}"		en																																																																																																																																										
		SL		email_admin_responses_subj		"Response submission for survey {SURVEYNAME} with results"		en																																																																																																																																										
		SL		email_admin_responses		"Hello,<br /><br />A new response was submitted for your survey '{SURVEYNAME}'.<br /><br />Click the following link to reload the survey:<br />{RELOADURL}<br /><br />Click the following link to see the individual response:<br />{VIEWRESPONSEURL}<br /><br />Click the following link to edit the individual response:<br />{EDITRESPONSEURL}<br /><br />View statistics by clicking here:<br />{STATISTICSURL}<br /><br /><br />The following answers were given by the participant:<br />{ANSWERTABLE}"		en																																																																																																																																										
		SL		surveyls_numberformat		0		en																																																																																																																																										
		SL		surveyls_survey_id		158192		fr																																																																																																																																										
		SL		surveyls_language		fr		fr																																																																																																																																										
		SL		surveyls_title		"Exemple de questionnaire EN/FR/DE"		fr																																																																																																																																										
		SL		surveyls_description		"Ce sondage montre toutes les types de questions de LimeSurvey et quelques options."		fr																																																																																																																																										
		SL		surveyls_welcometext		"<p>Ceci est le message d'accueil de votre sondage !! Vous pouvez l'éditer dans les paramètres du questionnaire.</p>"		fr																																																																																																																																										
		SL		surveyls_endtext		"<p>Ceci est le message de fin de votre questionnaire ! Un bon endroit pour vous remercier d'avoir répondu à ce questionnaire.</p>"		fr																																																																																																																																										
		SL		surveyls_url		http://www.limesurvey.org		fr																																																																																																																																										
		SL		surveyls_urldescription		"La description de l'URL de fin, ce sondage est distribué sous Licence GPL"		fr																																																																																																																																										
		SL		surveyls_email_invite_subj		"Invitation à participer à un questionnaire"		fr																																																																																																																																										
		SL		surveyls_email_invite		"Cher(e) {FIRSTNAME},<br /><br />Vous avez été invité à participer à un questionnaire.<br /><br />Celui-ci est intitulé :<br />""{SURVEYNAME}""<br /><br />""{SURVEYDESCRIPTION}""<br /><br />Pour participer, veuillez cliquer sur le lien ci-dessous.<br /><br />Cordialement,<br /><br />{ADMINNAME} ({ADMINEMAIL})<br /><br />----------------------------------------------<br />Cliquez ici pour remplir ce questionnaire :<br />{SURVEYURL}<br /><br />Si vous ne souhaitez pas participer à ce questionnaire et ne souhaitez plus recevoir aucune invitation, veuillez cliquer sur le lien suivant :<br />{OPTOUTURL}"		fr																																																																																																																																										
		SL		surveyls_email_remind_subj		"Rappel pour participer à un questionnaire"		fr																																																																																																																																										
		SL		surveyls_email_remind		"Cher(e) {FIRSTNAME},<br /><br />Vous avez été invité à participer à un questionnaire récemment.<br /><br />Nous avons pris en compte que vous n'avez pas encore complété le questionnaire, et nous vous rappelons que celui-ci est toujours disponible si vous souhaitez participer.<br /><br />Le questionnaire est intitulé :<br />""{SURVEYNAME}""<br /><br />""{SURVEYDESCRIPTION}""<br /><br />Pour participer, veuillez cliquer sur le lien ci-dessous.<br /><br />Cordialement,<br /><br />{ADMINNAME} ({ADMINEMAIL})<br /><br />----------------------------------------------<br />Cliquez ici pour faire le questionnaire:<br />{SURVEYURL}<br /><br />Si vous ne souhaitez pas participer à ce questionnaire et ne souhaitez plus recevoir aucune invitation, veuillez cliquer sur le lien suivant :<br />{OPTOUTURL}"		fr																																																																																																																																										
		SL		surveyls_email_register_subj		"Confirmation de l'inscription au questionnaire"		fr																																																																																																																																										
		SL		surveyls_email_register		"Cher(e){FIRSTNAME},<br /><br />Vous (ou quelqu'un utilisant votre adresse électronique) vous êtes enregistré pour participer à un questionnaire en ligne intitulé {SURVEYNAME}.<br /><br />Pour compléter ce questionnaire, cliquez sur le lien suivant :<br /><br />{SURVEYURL}<br /><br />Si vous avez des questions à propos de ce questionnaire, ou si vous ne vous êtes pas enregistré pour participer à celui-ci et croyez que ce courriel est une erreur, veuillez contacter {ADMINNAME} sur {ADMINEMAIL}"		fr																																																																																																																																										
		SL		surveyls_email_confirm_subj		"Confirmation de questionnaire complété"		fr																																																																																																																																										
		SL		surveyls_email_confirm		"Cher(e) {FIRSTNAME},<br /><br />Ce courriel vous confirme que vous avez complété le questionnaire intitulé {SURVEYNAME} et que votre réponse a été enregistrée. Merci pour votre participation.<br /><br />Si vous avez des questions à propos de ce courriel, veuillez contacter {ADMINNAME} sur {ADMINEMAIL}.<br /><br />Cordialement,<br /><br />{ADMINNAME}"		fr																																																																																																																																										
		SL		surveyls_dateformat		5		fr																																																																																																																																										
		SL		surveyls_alias				fr																																																																																																																																										
		SL		email_admin_notification_subj		"Soumission de réponse pour le questionnaire {SURVEYNAME}"		fr																																																																																																																																										
		SL		email_admin_notification		"Bonjour,<br /><br />Une nouvelle réponse a été soumise pour votre questionnaire '{SURVEYNAME}'.<br /><br />Cliquer sur le lien suivant pour recharger votre questionnaire :<br />{RELOADURL}<br /><br />Cliquer sur le lien suivant pour voir la réponse :<br />{VIEWRESPONSEURL}<br /><br />Cliquer sur le lien suivant pour éditer la réponse :<br />{EDITRESPONSEURL}<br /><br />Visualiser les statistiques en cliquant ici :<br />{STATISTICSURL}<br /><br />les réponses suivantes ont été données par le participant :<br />{ANSWERTABLE}"		fr																																																																																																																																										
		SL		email_admin_responses_subj		"Soumission de réponse pour le questionnaire {SURVEYNAME} avec résultats"		fr																																																																																																																																										
		SL		email_admin_responses		"Bonjour,<br /><br />Une nouvelle réponse a été soumise pour votre questionnaire '{SURVEYNAME}'.<br /><br />Cliquer sur le lien suivant pour recharger votre questionnaire :<br />{RELOADURL}<br /><br />Cliquer sur le lien suivant pour voir la réponse :<br />{VIEWRESPONSEURL}<br /><br />Cliquez sur le lien suivant pour éditer la réponse individuelle :<br />{EDITRESPONSEURL}<br /><br />Visualiser les statistiques en cliquant ici :<br />{STATISTICSURL}<br /><br /><br />les réponses suivantes ont été données par le participant :<br />{ANSWERTABLE}"		fr																																																																																																																																										
		SL		surveyls_numberformat		1		fr																																																																																																																																										
		SL		surveyls_survey_id		158192		it																																																																																																																																										
		SL		surveyls_language		it		it																																																																																																																																										
		SL		surveyls_title		"Sample LimeSurvey EN/FR/DE/IT"		it																																																																																																																																										
		SL		surveyls_description		"Questa indagine presenta tutti i tipi di domanda di LimeSurvey con alcune opzioni aggiuntive"		it																																																																																																																																										
		SL		surveyls_welcometext		"<p>Questo è il messaggio di benvenuto dell'indagine!!!</p><p>E' possibile modificarlo nelle impostazioni di indagine</p><p> </p>"		it																																																																																																																																										
		SL		surveyls_endtext		"<p>Questo è il messaggio di chiusura dell'indagine, dopo che il rispondente ha premuto INVIA.</p><p>E' possibile modificarlo nelle impostazioni di indagine</p>"		it																																																																																																																																										
		SL		surveyls_policy_notice		"Questo è il messaggio sui termini dei dati dell'indagine"		it																																																																																																																																										
		SL		surveyls_policy_error		"Questo è il messaggio di errore sui termini dei dati dell'indagine"		it																																																																																																																																										
		SL		surveyls_policy_notice_label		"Questa etichetta spiega i termini dei dati di indagine"		it																																																																																																																																										
		SL		surveyls_url				it																																																																																																																																										
		SL		surveyls_urldescription				it																																																																																																																																										
		SL		surveyls_email_invite_subj		"Invito per partecipare all'indagine"		it																																																																																																																																										
		SL		surveyls_email_invite		"Egregio/a {FIRSTNAME},<br /><br />è invitato a partecipare ad un'indagine on line.<br /><br />L'indagine è intitolata:<br />""{SURVEYNAME}""<br /><br />""{SURVEYDESCRIPTION}""<br /><br />Per partecipare fare click sul link in basso.<br /><br />Cordiali saluti,{ADMINNAME} ({ADMINEMAIL})<br /><br />----------------------------------------------<br />Fare click qui per accedere al questionario e rispondere alle domande relative:<br />{SURVEYURL}<br /><br />Se non si intende partecipare a questa indagine e non si vogliono ricevere altri inviti, si può cliccare sul seguente collegamento:<br />{OPTOUTURL}<br /><br />Se è presente in blacklist ma vuole partecipare a questa indagine e ricevere inviti, vada al seguente link:<br />{OPTINURL}"		it																																																																																																																																										
		SL		surveyls_email_remind_subj		"Promemoria per partecipare all'indagine"		it																																																																																																																																										
		SL		surveyls_email_remind		"Egregio/a {FIRSTNAME},<br />Recentemente ha ricevuto un invito a partecipare ad un'indagine on line.<br /><br />Abbiamo notato che non ha ancora completato il questionario. Con l'occasione Le ricordiamo che il questionario è ancora disponibile.<br /><br />L'indagine è intitolata:<br />""{SURVEYNAME}""<br /><br />""{SURVEYDESCRIPTION}""<br /><br />Per partecipare fare clic sul link qui sotto.<br /><br />Cordiali saluti,<br /><br />{ADMINNAME} ({ADMINEMAIL})<br /><br />----------------------------------------------<br />Fare clic qui per accedere all'indagine e rispondere al questionario:<br />{SURVEYURL}<br /><br />Se non si intende partecipare a questa indagine e non si vogliono ricevere altri inviti, si può cliccare sul seguente collegamento:<br />{OPTOUTURL}"		it																																																																																																																																										
		SL		surveyls_email_register_subj		"Conferma di registrazione all'indagine"		it																																																																																																																																										
		SL		surveyls_email_register		"Egregio/a {FIRSTNAME},<br /><br />Lei (o qualcuno che ha utilizzato il suo indirizzo e-mail) si è registrato per partecipare all'indagine on line intitolata {SURVEYNAME}.<br /><br />Per completare il questionario fare clic sul seguente indirizzo:<br /><br />{SURVEYURL}<br /><br />Se ha qualche domanda, o se non si è registrato e ritiene che questa e-mail ti sia pervenuta per errore, la preghiamo di contattare  {ADMINNAME} all'indirizzo {ADMINEMAIL}."		it																																																																																																																																										
		SL		surveyls_email_confirm_subj		"Confermare la partecipazione all&#039;indagine"		it																																																																																																																																										
		SL		surveyls_email_confirm		"Egregio/a {FIRSTNAME},<br /><br />Questa e-mail le è stata inviata per confermarle che ha completato correttamente il questionario intitolato {SURVEYNAME}  e che le sue risposte sono state salvate. Grazie per la partecipazione.<br /><br />Se ha ulteriori domande circa questo messaggio, la prego di contattare {ADMINNAME} all'indirizzo e-mail {ADMINEMAIL}.<br /><br />Cordiali saluti<br /><br />{ADMINNAME}"		it																																																																																																																																										
		SL		surveyls_dateformat		5		it																																																																																																																																										
		SL		surveyls_alias				it																																																																																																																																										
		SL		email_admin_notification_subj		"Invio di una risposta all'indagine {SURVEYNAME}"		it																																																																																																																																										
		SL		email_admin_notification		"Salve,<br /><br />Una nuova risposta é stata inviata per l'indagine '{SURVEYNAME}'.<br /><br />Fare click sul link seguente per vedere le risposte individuali:<br />{VIEWRESPONSEURL}<br /><br />Fare click sul link seguente per modificare le risposte individuali:<br />{EDITRESPONSEURL}<br /><br />Fare clic sul link seguente per visualizzare le statistiche:<br />{STATISTICSURL}"		it																																																																																																																																										
		SL		email_admin_responses_subj		"Invio di una risposta all'indagine {SURVEYNAME} con risultati"		it																																																																																																																																										
		SL		email_admin_responses		"Salve,<br /><br />Una nuova risposta è stata inviata dall'indagine '{SURVEYNAME}'.<br /><br />Fare clic sul link seguente per vedere la risposta individuale:<br />{VIEWRESPONSEURL}<br /><br />Fare clic sul link seguente per modificare la risposta individuale:<br />{EDITRESPONSEURL}<br /><br />Fare clic sul link seguente per visualizzare le statistiche:<br />{STATISTICSURL}<br /><br /><br />Le seguenti risposte sono state date dal partecipante:<br />{ANSWERTABLE}"		it																																																																																																																																										
		SL		surveyls_numberformat		0		it																																																																																																																																										
60		G	0	"Single choice question"		"The single choice questions group description"		en																																																																																																																																										
736		Q	5	q5		"5 point choice"		en		N	N	N		0	0																																																																																																																																			
64		G	2	"group nr2"				en																																																																																																																																										
391		Q	5	G02Q02	1	"another question here"		en		N	N	N		0	0																																						0	0																																		0					0																								0					0	1																							
65		G	3	"group nr3"				en																																																																																																																																										
392		Q	5	G03Q03	1	"One more question here"		en		N	N	N		0	0																																						0	0																																		0					0																								0					0	1																							
"""


def read_csv_and_return_array_of_dic(fileName):
    questions = []
    counter = 1
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            """
            Timestamp
            Email Address
            Proposal type
            Talk/Workshop title
            Abstract
            Notes to review for the organiser team
            Your name
            Your biography
            Additional speakers
            Audience knowledge level
            Speaker Release Agreement (CC BY-NC-SA 4.0)
            Twitter
            Linkendin
            Instagram
            Mastodon
            Will you require financial help if accepted?
            """
            questions.append({
                "id": counter,
                "title": row["Talk/Workshop title"],
                "abstract": row["Abstract"],
                "type": row["Proposal type"]
            })
            counter += 1
    return questions


def generate_limesurvey_txt(fileName, questions):
    with open(fileName, 'w', newline='') as csvfile:
        fieldnames = [
            "id", "related_id", "class", "type/scale", "name", "relevance",
            "text", "help", "language", "validation", "mandatory", "encrypted",
            "other", "default", "same_default", "same_script",
            "allowed_filetypes", "alphasort", "answer_width",
            "answer_width_bycolumn", "array_filter", "array_filter_exclude",
            "array_filter_style", "assessment_value", "category_separator",
            "choice_input_columns", "choice_title", "commented_checkbox",
            "commented_checkbox_auto", "cssclass", "date_format", "date_max",
            "date_min", "display_columns", "display_rows", "display_type",
            "dropdown_dates", "dropdown_dates_minute_step",
            "dropdown_dates_month_style", "dropdown_prefix",
            "dropdown_prepostfix", "dropdown_separators", "dropdown_size",
            "dualscale_headerA", "dualscale_headerB", "em_validation_q",
            "em_validation_q_tip", "em_validation_sq", "em_validation_sq_tip",
            "equals_num_value", "equation", "exclude_all_others",
            "exclude_all_others_auto", "hidden", "hide_tip", "input_boxes",
            "input_size", "label_input_columns", "location_city",
            "location_country", "location_defaultcoordinates",
            "location_mapheight", "location_mapservice", "location_mapwidth",
            "location_mapzoom", "location_nodefaultfromip", "location_postal",
            "location_state", "max_answers", "max_filesize",
            "max_num_of_files", "max_num_value", "max_num_value_n",
            "max_subquestions", "maximum_chars", "min_answers",
            "min_num_of_files", "min_num_value", "min_num_value_n",
            "multiflexible_checkbox", "multiflexible_max", "multiflexible_min",
            "multiflexible_step", "num_value_int_only", "numbers_only",
            "other_comment_mandatory", "other_numbers_only",
            "other_replace_text", "page_break", "parent_order", "placeholder",
            "prefix", "printable_help", "public_statistics", "random_group",
            "random_order", "rank_title", "repeat_headings", "reverse",
            "samechoiceheight", "samelistheight", "scale_export",
            "show_comment", "show_grand_total", "show_title", "show_totals",
            "showpopups", "slider_accuracy", "slider_custom_handle",
            "slider_default", "slider_default_set", "slider_handle",
            "slider_layout", "slider_max", "slider_middlestart", "slider_min",
            "slider_orientation", "slider_rating", "slider_reset",
            "slider_reversed", "slider_separator", "slider_showminmax",
            "statistics_graphtype", "statistics_showgraph",
            "statistics_showmap", "suffix", "text_input_columns",
            "text_input_width", "time_limit", "time_limit_action",
            "time_limit_countdown_message", "time_limit_disable_next",
            "time_limit_disable_prev", "time_limit_message",
            "time_limit_message_delay", "time_limit_message_style",
            "time_limit_timer_style", "time_limit_warning",
            "time_limit_warning_2", "time_limit_warning_2_display_time",
            "time_limit_warning_2_message", "time_limit_warning_2_style",
            "time_limit_warning_display_time", "time_limit_warning_message",
            "time_limit_warning_style", "use_dropdown",
            "value_range_allows_missing"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerow({"class": "S", "name": "sid"})
        writer.writerow({"class": "S", "name": "gsid"})
        writer.writerow({
            "class": "S",
            "name": "admin",
            "text": "Helio Loureiro"
        })
        writer.writerow({
            "class": "S",
            "name": "adminemail",
            "text": "Helio@Loureiro.eng.br"
        })
        writer.writerow({"class": "S", "name": "anonymized", "text": "Y"})
        writer.writerow({"class": "S", "name": "format", "text": "G"})
        writer.writerow({"class": "S", "name": "savetimings", "text": "I"})
        writer.writerow({
            "class": "S",
            "name": "template",
            "text": "bootswatch"
        })
        writer.writerow({"class": "S", "name": "language", "text": "en"})
        writer.writerow({"class": "S", "name": "allowregister", "text": "N"})
        writer.writerow({"class": "S", "name": "htmlemail", "text": "Y"})
        writer.writerow({
            "class": "S",
            "name": "sendconfirmation",
            "text": "Y"
        })
        writer.writerow({
            "class": "S",
            "name": "tokenanswerspersistence",
            "text": "Y"
        })
        writer.writerow({"class": "S", "name": "usecaptcha", "text": "E"})
        writer.writerow({"class": "S", "name": "usetokens", "text": "N"})
        writer.writerow({
            "class": "S",
            "name": "bounce_email",
            "text": "helio@loureiro.eng.br"
        })
        writer.writerow({
            "class": "S",
            "name": "alloweditaftercompletion",
            "text": "Y"
        })
        writer.writerow({"class": "SL", "name": "surveyls_survey_id"})
        writer.writerow({
            "class": "SL",
            "name": "surveyls_language",
            "text": "en",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "surveyls_title",
            "text": "testing survey",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "surveyls_description",
            "text":
            "This survey show all question type of LimeSurvey with some option",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "surveyls_welcometext",
            "text":
            "<p>This is the welcome text for the survey! You can can edit it in the survey properties.</p>",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "surveyls_endtext",
            "text":
            "<p>This is the end message for the survey! A good place to thank you to answer to this survey.</p>",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "surveyls_url",
            "text": "http://www.limesurvey.org",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "surveyls_urldescription",
            "text":
            "The end URL description of your survey. This URL can be automatically load when survey is completed.",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "surveyls_email_invite_subj",
            "text": "Invitation to participate in survey",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "surveyls_email_invite",
            "text":
            """Dear {FIRSTNAME},<br /><br />You have been invited to participate in a survey.<br /><br />The survey is titled:<br />"{SURVEYNAME}"<br /><br />"{SURVEYDESCRIPTION}"<br /><br />To participate, please click on the link below.<br /><br />Sincerely,<br /><br />{ADMINNAME} ({ADMINEMAIL})<br /><br />----------------------------------------------<br />Click here to do the survey:<br />{SURVEYURL}<br /><br />If you do not want to participate in this survey and don't want to receive any more invitations please click the following link:<br />{OPTOUTURL}""",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "surveyls_email_remind_subj",
            "text": "Reminder to participate in survey",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "surveyls_email_remind",
            "text":
            """Dear {FIRSTNAME},<br /><br />Recently we invited you to participate in a survey.<br /><br />We note that you have not yet completed the survey, and wish to remind you that the survey is still available should you wish to take part.<br /><br />The survey is titled:<br />"{SURVEYNAME}"<br /><br />"{SURVEYDESCRIPTION}"<br /><br />To participate, please click on the link below.<br /><br />Sincerely,<br /><br />{ADMINNAME} ({ADMINEMAIL})<br /><br />----------------------------------------------<br />Click here to do the survey:<br />{SURVEYURL}<br /><br />If you do not want to participate in this survey and don't want to receive any more invitations please click the following link:<br />{OPTOUTURL}""",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "surveyls_email_register_subj",
            "text": "Survey registration confirmation",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "surveyls_email_register",
            "text":
            """Dear {FIRSTNAME},<br /><br />You, or someone using your email address, have registered to participate in an online survey titled {SURVEYNAME}.<br /><br />To complete this survey, click on the following URL:<br /><br />{SURVEYURL}<br /><br />If you have any questions about this survey, or if you did not register to participate and believe this email is in error, please contact {ADMINNAME} at {ADMINEMAIL}.""",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "surveyls_email_confirm_subj",
            "text": "Confirmation of completed survey",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "surveyls_email_confirm",
            "text":
            """Dear {FIRSTNAME},<br /><br />This email is to confirm that you have completed the survey titled {SURVEYNAME} and your response has been saved. Thank you for participating.<br /><br />If you have any further questions about this email, please contact {ADMINNAME} at {ADMINEMAIL}.<br /><br />Sincerely,<br /><br />{ADMINNAME}""",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "email_admin_notification_subj",
            "text": "Response submission for survey {SURVEYNAME}",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "email_admin_notification",
            "text":
            """Hello,<br /><br />A new response was submitted for your survey '{SURVEYNAME}'.<br /><br />Click the following link to reload the survey:<br />{RELOADURL}<br /><br />Click the following link to see the individual response:<br />{VIEWRESPONSEURL}<br /><br />Click the following link to edit the individual response:<br />{EDITRESPONSEURL}<br /><br />View statistics by clicking here:<br />{STATISTICSURL}""",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "email_admin_responses_subj",
            "text": "Response submission for survey {SURVEYNAME} with results",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "email_admin_responses",
            "text":
            """Hello,<br /><br />A new response was submitted for your survey '{SURVEYNAME}'.<br /><br />Click the following link to reload the survey:<br />{RELOADURL}<br /><br />Click the following link to see the individual response:<br />{VIEWRESPONSEURL}<br /><br />Click the following link to edit the individual response:<br />{EDITRESPONSEURL}<br /><br />View statistics by clicking here:<br />{STATISTICSURL}<br /><br /><br />The following answers were given by the participant:<br />{ANSWERTABLE}""",
            "language": "en"
        })
        writer.writerow({
            "class": "SL",
            "name": "surveyls_numberformat",
            "language": "en"
        })
        """
        writer.writerow({
            "id": "60",
            "class": "G",
            "type/scale": "0",
            "name": "Single choice question",
            "text": "The single choice questions group description",
            "language": "en"
        })
        writer.writerow({
            "id": "736",
            "class": "Q",
            "type/scale": "5",
            "name": "q5",
            "text": "5 point choice",
            "language": "en",
            "mandatory": "N",
            "encrypted": "N",
            "other": "N",
            "same_default": "0",
            "same_script": "0"
        })
        writer.writerow({
            "id": "64",
            "class": "G",
            "type/scale": "2",
            "name": "group nr2",
            "language": "en"
        })
        writer.writerow({
            "id": "391",
            "class": "Q",
            "type/scale": "5",
            "name": "G02Q02 title of the talk",
            "text": "another question here",
            "language": "en",
            "mandatory": "N",
            "encrypted": "N",
            "other": "N",
            "same_default": "0",
            "same_script": "0"
        })
        writer.writerow({
            "id": "65",
            "class": "G",
            "type/scale": "3",
            "name": "group nr3 description",
            "language": "en"
        })
        writer.writerow({
            "id": "392",
            "class": "Q",
            "type/scale": "5",
            "name": "G03Q03 title of the talk",
            "text": "another question here number 3",
            "language": "en",
            "mandatory": "N",
            "encrypted": "N",
            "other": "N",
            "same_default": "0",
            "same_script": "0"
        })
        writer.writerow({
            "id": "66",
            "class": "G",
            "type/scale": "4",
            "name": "group nr4 description",
            "language": "en"
        })
        writer.writerow({
            "id": "393",
            "class": "Q",
            "type/scale": "5",
            "name": "G04Q04 one more title of the talk",
            "text": "another question here number 4",
            "language": "en",
            "mandatory": "N",
            "encrypted": "N",
            "other": "N",
            "same_default": "0",
            "same_script": "0"
        })
        """
        counter_group = 60
        counter_talk = 390
        scale = 1
        for q in questions:
            abstract = re.sub("\n", "&nbsp;\n", q["abstract"])
            writer.writerow({
                "id": str(counter_group),
                "class": "G",
                "type/scale": str(scale),
                "name": q["type"],
                "language": "en"
            })

            writer.writerow({
                "id":
                str(counter_talk),
                "class":
                "Q",
                "type/scale":
                "5",
                "name":
                q["title"][:10],
                "text":
                "<h2>Title: " + q["title"] + "</h2>\n\n<h3>Abstract:</h3>\n" +
                abstract,
                "language":
                "en",
                "mandatory":
                "N",
                "encrypted":
                "N",
                "other":
                "N",
                "same_default":
                "0",
                "same_script":
                "0"
            })
            print("title:", q["title"], ", type:", q["type"])

            counter_group += 1
            counter_talk += 1
            scale += 1

            # for tests only
            if scale > 30:
                break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=
        'Script to convert CPF\'s CSV file into TXT that can be imported by limesurvey'
    )
    parser.add_argument('--csvfile',
                        required=True,
                        help='The CSV file exported from the Google forms')
    parser.add_argument(
        '--output',
        required=True,
        help=
        'The TXT formatted file to be created and later imported into limesurvey'
    )

    args = parser.parse_args()

    questions = read_csv_and_return_array_of_dic(args.csvfile)
    generate_limesurvey_txt(args.output, questions)
