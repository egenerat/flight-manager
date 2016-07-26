# coding=utf-8

CONCORDE_PANEL_AVAILABLE_HTML = u'<a href="compte\.php\?page=alliances&tc=10&action=1" class="lien">Détails</a>'
ALLIANCE_CONCORDE_PATTERN_HTML = u'<td class="Aalliances2"><a href="compte\.php\?page=alliances1&action=6&placer=2&la_variete=(\d{6})" class="lien">Retirer</a></td>'
PM_NB_REGEX = u'<li><a href="compte\.php\?page=mp" class="speciale">MP \(.*?(\d+).*?\)</a></li>'
PM_BOX_PM_IDS_REGEX = u'<a href="compte\.php\?page=mp1&id_mp=(\d+)" class="lien">Les impôts</a> &nbsp;<font color="red">Nouveau !</font></td>'
PM_BEGIN_MESSAGE_PATTERN = '<td class="mp4_1" colSpan=3><br />'
PM_END_MESSAGE_PATTERN = '<SCRIPT language=javascript src="images/editPost.js"></SCRIPT>'