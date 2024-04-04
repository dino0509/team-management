from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime;
from django.utils.timezone import make_aware
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re

from .models import TeamMember

# Default page.
# Lists all the current team members
def list(request):
    members = TeamMember.objects.all()
    context = {
        "member_list": members,
        "size": len(members),
    }
    return render(request, "member_management/list.html", context)

# Loads a form to enter the details of a new team member
def add(request):
    return render(request, "member_management/add.html")

# Creates a new team member from the request parameters
# this method is invoked when the add form is submitted
def submit_add(request):
    if 'back' in request.POST:
        return HttpResponseRedirect(reverse("member_management:list"))

    m = TeamMember(first_name = request.POST["first_name"].strip(),
        last_name = request.POST["last_name"].strip(),
        email = request.POST["email"].strip(),
        phone = request.POST["phone"].strip(),
        is_admin = request.POST["is_admin"],
        add_date = make_aware(datetime.datetime.now()),)

    if validate_member_details(m):
        m.save()
        return HttpResponseRedirect(reverse("member_management:list"))
    else:
        members = TeamMember.objects.all()
        context = {
            "member_list": members,
            "size": len(members),
            "error_message": "Invalid Member Details",
        }
        return render(request, "member_management/list.html", context)

# Loads a form to update the details of an existing team member
def edit(request, member_id):
    try:
        member = TeamMember.objects.get(id=member_id)
    except TeamMember.DoesNotExist:
        members = TeamMember.objects.all()
        context = {
            "member_list": members,
            "size": len(members),
            "error_message": "No team member found with ID " + str(member_id),
        }
        return render(request, "member_management/list.html", context)

    context = {
        "member": member,
    }
    return render(request, "member_management/edit.html", context)

# Updates a team member from the request parameters
# this method is invoked when the edit form is submitted
def submit_edit(request, member_id):
    if 'back' in request.POST:
        return HttpResponseRedirect(reverse("member_management:list"))

    try:
        member = TeamMember.objects.get(id=member_id)
    except TeamMember.DoesNotExist:
        members = TeamMember.objects.all()
        context = {
            "member_list": members,
            "size": len(members),
            "error_message": "No team member found with ID " + str(member_id),
        }
        return render(request, "member_management/list.html", context)

    if 'delete' in request.POST:
        member.delete()
        return HttpResponseRedirect(reverse("member_management:list"))
    else:
        member.first_name = request.POST['first_name'].strip()
        member.last_name = request.POST['last_name'].strip()
        member.email = request.POST['email'].strip()
        member.phone = request.POST['phone'].strip()
        member.is_admin = request.POST['is_admin']
        if validate_member_details(member):
            member.save()
            return HttpResponseRedirect(reverse("member_management:list"))
        else:
            members = TeamMember.objects.all()
            context = {
                "member_list": members,
                "size": len(members),
                "error_message": "Invalid Member Details",
            }
            return render(request, "member_management/list.html", context)


# Validate the Team Member details
# Returns True if the Team member details are valid
# Returns False if not
def validate_member_details(member):
# first and last name should only contain letters and spaces
    name_pattern = re.compile("^[a-zA-Z ]+$")
# phone number should only contain numbers
    phone_pattern = re.compile("^[0-9]+$")
    if name_pattern.match(member.first_name) is None:
        return False
    if name_pattern.match(member.last_name) is None:
        return False
    # Phone number can be empty
    if member.phone != "" and phone_pattern.match(member.phone) is None:
        return False

# validate the email
    try:
        validate_email(member.email)
    except ValidationError:
        return False
    else:
        return True
