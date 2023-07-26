import os
import sys
import distutils.dir_util
import shutil
import urllib.parse
import urllib.request


def hips_uri_to_path(hips_uri_path):
    # this expects a fully-populated URI. If any component of the URI is ommitted, currently this function will
    # only return up to that portion of the path. e.g. if "project?Vessel=vessel;Day=2000-001" is provided,
    # this function will return "project\vessel\2000-001" without the rest of the path
    
    # this function can handle multiple lines referenced in the URI, and returns a list of paths
    project_paths = []
    project = ""
    components = urllib.parse.urlparse(hips_uri_path)
    
    if components.netloc:  # path is network location
        project = r'\\' + components.netloc + components.path
    else:
        project = components.path
        if project.startswith('/'):
            project = project[1:]
    
    # switch the slashes
    project = project.replace("/", "\\")
    
    # remove the HIPS file reference
    project = os.path.split(project)[0]
    
    # for each unique query, append to the source path
    if components.query:
        for query in components.query.split("&"):
            line_ref = urllib.parse.parse_qsl(query)
            if line_ref:
                project_paths.append(project) # start with the project folder
                for item in line_ref:         # add each query item to the last list entry
                    project_paths[-1] += "\\" + item[1]
    else:  # if there's no query, just return the project path
        project_paths.append(project)
    
    return project_paths


def hips_path_to_uri(full_project_path, vessel="", day="", line=""):
    project_uri = ""
    if not full_project_path[-5:] == '.hips':
        # path is project folder, not HIPS file... probably
        project_root, project_name = os.path.split(full_project_path)
        full_project_path = project_root + '\\' + project_name + '\\' + project_name + '.hips'

    # see if it's already a network path, otherwise use urllib
    if full_project_path[:2] == '\\\\':
        project_uri = 'file:' + full_project_path.replace("/", "\\")
    else:
        # project_uri = urllib.parse.urljoin(
        #     'file:',
        #     urllib.request.pathname2url(full_project_path.replace("/", "\\"))
        #     )
        project_uri = 'file:///' + full_project_path.replace("/", "\\")

    # set a wildcard when the child value are specified but not the parents
    if not vessel and (day or line):
        vessel = "*"
    if not day and line:
        day = "*"

    # construct the URI
    if vessel:
        project_uri += '?Vessel=' + vessel
    if day:
        project_uri += ';Day=' + day
    if line:
        project_uri += ';Line=' + line

    return project_uri


def hips_path_to_uri_surface(full_project_path, surface_name):
    project_uri = ""
    if full_project_path[-5:] == '.hips':
        project_root, project_name = os.path.split(full_project_path)
        full_project_path = project_root + '\\'

    # see if it's already a network path, otherwise use urllib
    if full_project_path[:2] == '\\\\':
        project_uri = 'file:' + full_project_path.replace("/", "\\")
    else:
        project_uri = urllib.parse.urljoin(
            'file:',
            urllib.request.pathname2url(full_project_path.replace("/", "\\"))
            )

    # construct the URI
    if surface_name:
        project_uri += "/" + surface_name

    return project_uri


def format_export_hips_file(file):
    with open('{}_temp.txt'.format(file), 'r') as temp:
        with open('{}.txt'.format(file), 'w') as sondes_extraites:
            for index, line in enumerate(temp, 1):
                items = line.split(',')
                sondes_extraites.write('{},{},{},{},{},{}'.format(
                    index, items[1], items[0], items[2], items[3], items[4]))
    os.remove('{}_temp.txt'.format(file))
